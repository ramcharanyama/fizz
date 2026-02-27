"""
AI PII Redactor - FastAPI Application
Multi-Modal Privacy Preservation Framework

Railway-safe entry point.
- No imports that can crash at module load
- MySQL is lazy (only inside route handlers)
- App always boots, even if DB or engines are unavailable
"""

import os
import time
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ── Logging ──────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# ── Startup timestamp ───────────────────────────────────
START_TIME = time.time()

# ── FastAPI app ──────────────────────────────────────────
app = FastAPI(
    title="AI PII Redactor",
    description="Multi-Modal Privacy Preservation Framework",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS (allow all origins for hackathon demo) ─────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition", "Content-Type", "Content-Length"],
)

# ── Register routers (lazy-loaded orchestrator inside) ──
try:
    from app.routers import redaction
    app.include_router(redaction.router)
    logger.info("Redaction router registered successfully")
except Exception as e:
    logger.warning("Could not load redaction router: %s", e)


# ── Routes ──────────────────────────────────────────────
@app.get("/")
async def root():
    """Health / info route. Always works, no DB required."""
    uptime = time.time() - START_TIME
    return {
        "status": "ok",
        "name": "AI PII Redactor",
        "version": "1.0.0",
        "description": "Multi-Modal Privacy Preservation Framework",
        "uptime_seconds": round(uptime, 2),
        "docs": "/docs",
        "api_base": "/api/v1",
        "environment": os.getenv("RAILWAY_ENVIRONMENT", "development"),
    }


@app.get("/db-test")
async def db_test():
    """Verify MySQL database connectivity. Lazy — only connects when called."""
    try:
        import pymysql

        conn = pymysql.connect(
            host=os.getenv("MYSQLHOST", "127.0.0.1"),
            port=int(os.getenv("MYSQLPORT", "3306")),
            user=os.getenv("MYSQLUSER", "root"),
            password=os.getenv("MYSQLPASSWORD", ""),
            database=os.getenv("MYSQLDATABASE", "railway"),
            cursorclass=pymysql.cursors.DictCursor,
            connect_timeout=10,
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 AS alive")
            row = cursor.fetchone()
        conn.close()
        return {
            "status": "connected",
            "database": os.getenv("MYSQLDATABASE", "railway"),
            "host": os.getenv("MYSQLHOST", "unknown"),
            "result": row,
        }
    except ImportError:
        return {"status": "error", "detail": "pymysql is not installed"}
    except Exception as exc:
        logger.error("Database connection failed: %s", exc)
        return {"status": "error", "detail": str(exc)}


# ── Lifecycle events ────────────────────────────────────
@app.on_event("startup")
async def startup_event():
    port = os.getenv("PORT", "8000")
    logger.info("🛡️  AI PII Redactor starting on 0.0.0.0:%s", port)
    logger.info("📚 API docs → /docs")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛡️  AI PII Redactor shutting down...")


# ── Uvicorn entrypoint (Railway uses Procfile) ──────────
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
        log_level="info",
    )
