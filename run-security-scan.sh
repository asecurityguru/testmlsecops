#!/bin/bash

echo "======================================"
echo "MLSecOps Local Security Scan"
echo "======================================"
echo ""

# SAST - Bandit
echo "🔍 Running SAST with Bandit..."
echo "--------------------------------------"
bandit -r . -ll -f txt
echo ""

# Show summary
echo "======================================"
echo "✅ Security Scan Complete!"
echo "======================================"
echo ""
echo "📊 Summary:"
echo "- SAST: Bandit detected code security issues"
echo "- SCA: Use 'pip-audit' or 'safety scan' for dependency checks"
echo ""
echo "💡 Tip: Fix high/critical issues before deployment"
