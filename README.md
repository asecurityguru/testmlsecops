# MLSecOps Demo: SAST & SCA with GitHub Actions

A simple demonstration of integrating security scanning into ML projects using GitHub Actions.

## 🔒 Security Tools Implemented

### 1. SAST (Static Application Security Testing)
- **Bandit**: Scans Python code for common security issues
- **Semgrep**: Advanced static analysis with security patterns

### 2. SCA (Software Composition Analysis)
- **Safety**: Checks Python dependencies for known vulnerabilities
- **pip-audit**: Audits Python packages for security issues

## 🚀 Quick Start

### Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Run SAST with Bandit
pip install bandit
bandit -r . -ll

# Run SCA with Safety
pip install safety
safety check -r requirements.txt

# Run SCA with pip-audit
pip install pip-audit
pip-audit -r requirements.txt
```

## 🔍 Security Issues Detected

The code intentionally includes security issues for demonstration:

### Code Issues (SAST):
1. **Hardcoded credentials** (line 35)
2. **Unsafe pickle deserialization** (line 11)
3. **SQL injection vulnerability** (line 29)

### Dependency Issues (SCA):
- Outdated packages with known CVEs
- Vulnerable versions of pandas, scikit-learn, flask

## 📊 GitHub Actions Workflow

The workflow automatically:
1. Runs on push/PR to main branch
2. Executes SAST scans (Bandit, Semgrep)
3. Performs SCA checks (Safety, pip-audit)
4. Uploads security reports as artifacts
5. Fails build if critical issues found

## 🛠️ Fixing Security Issues

### Code Fixes:
```python
# Use environment variables for secrets
import os
API_KEY = os.getenv('API_KEY')

# Use joblib instead of pickle
from joblib import dump, load

# Use parameterized queries
query = "SELECT * FROM data WHERE id = ?"
```

### Dependency Fixes:
```bash
# Update requirements.txt
pandas>=2.0.0
scikit-learn>=1.3.0
numpy>=1.24.0
flask>=3.0.0
requests>=2.31.0
```

## 📝 Reports Generated

- `bandit-report.json`: SAST findings
- `safety-report.json`: SCA vulnerability report
- `pip-audit-report.json`: Package audit results
- Semgrep results in Actions logs

## 🎯 Best Practices

1. **Shift Left**: Run security scans early in development
2. **Automate**: Integrate into CI/CD pipeline
3. **Monitor**: Track security metrics over time
4. **Remediate**: Fix high/critical issues immediately
5. **Update**: Keep dependencies current

## 📚 Resources

- [Bandit Documentation](https://bandit.readthedocs.io/)
- [Safety Documentation](https://pyup.io/safety/)
- [Semgrep Rules](https://semgrep.dev/explore)
- [OWASP Top 10 ML](https://owasp.org/www-project-machine-learning-security-top-10/)
