import re


def analyze_complaint(text):

    text_lower = text.lower()

    category = "Unknown"
    severity = "Low"
    laws = []
    safety_tips = []

    extracted_data = {
        "phones": [],
        "emails": [],
        "urls": [],
        "amounts": [],
        "upi_ids": []
    }

    # =========================
    # OTP / Banking Scam
    # =========================

    if any(word in text_lower for word in [
        "otp",
        "bank",
        "verification code",
        "account blocked"
    ]):

        category = "OTP / Banking Scam"
        severity = "High"

        laws = [
            "IPC 420",
            "IT Act 66C",
            "IT Act 66D"
        ]

        safety_tips = [
            "Do not share OTP with anyone",
            "Change banking passwords immediately",
            "Block suspicious numbers",
            "Enable two-factor authentication",
            "Report incident on cybercrime.gov.in"
        ]

    # =========================
    # Phishing Attack
    # =========================

    elif any(word in text_lower for word in [
        "link",
        "password",
        "login",
        "fake website"
    ]):

        category = "Phishing Attack"
        severity = "High"

        laws = [
            "IT Act 66C",
            "IT Act 66D"
        ]

        safety_tips = [
            "Avoid clicking suspicious links",
            "Change compromised passwords",
            "Enable MFA on accounts",
            "Verify website authenticity"
        ]

    # =========================
    # Fake Loan Scam
    # =========================

    elif any(word in text_lower for word in [
        "loan",
        "processing fee",
        "instant loan"
    ]):

        category = "Fake Loan Scam"
        severity = "Medium"

        laws = [
            "IPC 420",
            "IT Act 66D"
        ]

        safety_tips = [
            "Never pay advance loan fees",
            "Verify company registration",
            "Avoid suspicious loan apps"
        ]

    # =========================
    # Job Scam
    # =========================

    elif any(word in text_lower for word in [
        "job",
        "interview",
        "registration fee",
        "work from home"
    ]):

        category = "Fake Job Scam"
        severity = "Medium"

        laws = [
            "IPC 420",
            "IT Act 66D"
        ]

        safety_tips = [
            "Verify recruiters carefully",
            "Avoid paying registration fees",
            "Check official company website"
        ]

    # =========================
    # Sextortion
    # =========================

    elif any(word in text_lower for word in [
        "video call",
        "private photo",
        "blackmail",
        "morphed"
    ]):

        category = "Sextortion / Blackmail"
        severity = "Critical"

        laws = [
            "IPC 384",
            "IPC 354D",
            "IT Act 67"
        ]

        safety_tips = [
            "Do not panic",
            "Preserve screenshots and evidence",
            "Block and report offender",
            "Contact cybercrime authorities immediately"
        ]

    # =========================
    # Investment Scam
    # =========================

    elif any(word in text_lower for word in [
        "investment",
        "crypto",
        "double money",
        "trading"
    ]):

        category = "Investment / Crypto Scam"
        severity = "High"

        laws = [
            "IPC 420",
            "IT Act 66D"
        ]

        safety_tips = [
            "Avoid unrealistic investment promises",
            "Verify trading platforms",
            "Do not transfer funds quickly"
        ]

    # =========================
    # UPI Fraud
    # =========================

    elif any(word in text_lower for word in [
        "upi",
        "paytm",
        "phonepe",
        "gpay",
        "google pay"
    ]):

        category = "UPI Fraud"
        severity = "High"

        laws = [
            "IPC 420",
            "IT Act 66C",
            "IT Act 66D"
        ]

        safety_tips = [
            "Never approve unknown collect requests",
            "Verify UPI IDs before payment",
            "Disable suspicious accounts"
        ]

    # =========================
    # Evidence Extraction
    # =========================

    phones = re.findall(r'\b\d{10}\b', text)

    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+',
        text
    )

    urls = re.findall(
        r'https?://\S+|www\.\S+',
        text
    )

    amounts = re.findall(
        r'₹\s?\d+|\d+\s?rupees|\d+\s?rs',
        text_lower
    )

    upi_ids = re.findall(
        r'[\w\.-]+@[\w]+',
        text
    )

    extracted_data["phones"] = phones
    extracted_data["emails"] = emails
    extracted_data["urls"] = urls
    extracted_data["amounts"] = amounts
    extracted_data["upi_ids"] = upi_ids

    # =========================
    # AI-style Summary
    # =========================

    summary = f"""
Cyber Crime Complaint Summary

Complaint Category:
{category}

Threat Severity:
{severity}

Applicable Legal Sections:
{", ".join(laws)}

Complaint Analysis:
The citizen reported a suspected cyber fraud incident
related to {category.lower()}.

The system identified possible indicators of cybercrime
activity based on complaint keywords and extracted evidence.

Recommended Actions:
- Preserve screenshots and digital evidence
- Report incident at cybercrime.gov.in
- Avoid further interaction with suspects
- Secure banking and social media credentials
"""

    return {
        "category": category,
        "severity": severity,
        "laws": laws,
        "safety_tips": safety_tips,
        "extracted_data": extracted_data,
        "summary": summary
    }