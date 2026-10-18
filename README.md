# CENG413 HW-1: Flask app in Docker
1. Build: `docker build -t ceng413-app:1.0 .`
2. Run: `docker run --rm -p 8080:8080 -e APP_NAME=my-app ceng413-app:1.0`
3. Test: `curl http://localhost:8080/health` → `{"status":"ok"}`
4. Endpoints: `/`, `/health`, `/time`. Settings (env vars): `PORT` (default 8080), `APP_NAME`.
