# Vault

Vault is a centralized system for securely storing, accessing, and managing secrets.

A secret can be:
- Database passwords
- API keys
- TLS certificates
- SSH keys
- Cloud credentials
- Encryption keys

Core Concepts:
- __Authentication__ (Auth Methods). Common auth methods:
  - Token
  - Kubernetes
  - AWS IAM
  - LDAP
  - GitHub
  - AppRole
- Policies (__Authorization__): to control who can access what
- Secrets Engines: define how secrets are stored or generated:
  - Key-Value: Static secrets
  - Database: Dynamic DB credentials
  - PKI: TLS certificates
  - AWS: Dynamic AWS credentials

For HA, Vault nodes form a cluster and elect a leader.

## Example

```
# Enable KV engine:
vault secrets enable -path=secret kv-v2

# Store secret:
vault kv put secret/db username=admin password=123456

# Retrieve secret:
vault kv get secret/db
```


