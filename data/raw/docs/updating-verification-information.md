---
url: https://docs.xendit.co/docs/updating-verification-information
title: Updating Verification Information
description: ''
section: docs
scraped_at: '2026-04-23T06:17:57.870401Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatformSet up sub-accountsAPI Verification for DevelopersLegacy
  Account Holder API
- Documentation
- xenPlatform
- Set up sub-accounts
- API Verification for Developers
- Legacy Account Holder API
---
# Updating Verification Information

Your verification request may be rejected due to missing information, invalid documents, etc. You will receive an Account Holder webhook notification that will give you specific information to update the Account Holder accordingly. To update your merchant’s information, you must update the `Account Holder` object with the parameters that need to be revised.

**Sample callback payload:**

JSON

```
{
    "created": "2021-01-01T10:00:00Z",
    "event": "account_holder.kyc.status",
    "business_id": "5fe2b0137b7d62542fe6d7de",
    "data": {
        "id": "57fb4e076fa3fa296b7f5a97",
        "created": "2021-01-01T10:00:00Z",
        "updated": "2021-01-01T10:00:00Z",
        "kyc": {
            "status": "RESUBMISSION_REQUIRED",
            "verified_at": "2021-01-01T10:00:00Z",
            "requested_at": "2021-01-01T10:00:00Z",
            "failure_reasons": [
                {
                    "field": "website_url",
                    "message": "Website is Invalid"
                }
            ]
        }
    }
}
```

JSON

Copy

## Sample requests

```
PATCH https://api.xendit.co/account_holders/{id}
```

Plain text

Copy

## Update website URL

```
{
    "website_url": "sample-marketplace.xendit.com"
}
```

JSON

Copy

## Update KYC documents

```
{
    "kyc_documents": [
        {
            "country": "PH",
            "type": "LATEST_GIS_DOCUMENT",
            "file_id": "63f8719642f5856dc9feje7"
        }
    ]
}
```

JSON

Copy
