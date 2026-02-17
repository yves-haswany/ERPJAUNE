from fastapi import Request, HTTPException


def get_tenant_id(request: Request):
    tenant_id = request.state.tenant_id
    if not tenant_id:
        raise HTTPException(status_code=400, detail="Tenant header missing")
    return tenant_id
