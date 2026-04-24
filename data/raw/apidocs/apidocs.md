---
url: "https://docs.xendit.co/apidocs"
title: "Quick setup"
description: ""
section: "apidocs"
scraped_at: "2026-04-23T06:03:44.725189Z"
source: "https://docs.xendit.co"
breadcrumbs:
  - "API DocumentationOverview"
  - "API Documentation"
  - "Overview"
internal_links:
  - "https://docs.xendit.co/apidocs"
  - "https://docs.xendit.co/apidocs/accounts-misc-introduction"
  - "https://docs.xendit.co/apidocs/bi-snap"
  - "https://docs.xendit.co/apidocs/introduction"
  - "https://docs.xendit.co/apidocs/introduction-1"
  - "https://docs.xendit.co/apidocs/others-introduction"
  - "https://docs.xendit.co/apidocs/payment-link"
  - "https://docs.xendit.co/apidocs/payouts-introduction"
  - "https://docs.xendit.co/apidocs/quick-setup"
  - "https://docs.xendit.co/apidocs/rate-limits"
  - "https://docs.xendit.co/apidocs/webhook-behavior"
---

# Quick setup

## API format

The Xendit API is organized around REST. Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors. We use built-in HTTP features and HTTP verbs, which are understood by off-the-shelf HTTP clients. JSON is returned by all API responses, including errors.

## Authentication

### **Getting Started with Xendit APIs**

To begin exploring our APIs, please ensure you have registered an account on our dashboard [here](https://dashboard.xendit.co/). You can obtain and manage your API keys (for both test and live environments) in the [API Keys Settings](https://dashboard.xendit.co/settings/developers#api-keys) section.

### **Authentication**

To authenticate your API requests, include your secret API key in the request. Follow these steps:

1. Generate a secret API key
2. Retrieve your secret API key from the Dashboard.
3. Choose [Basic Access Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) (BASIC AUTH).
4. Use the BASIC AUTH format: `{username}:{password}`
5. Enter your Secret API key as the username and leave the password field empty. Ensure you include a colon (`:`) at the end.
6. Encode the resulting value using [Base64](https://en.wikipedia.org/wiki/Base64).
7. Include the Base64-encoded value in the Authorization header of your requests.

### **Important Considerations**

- **Security:** Keep your API keys confidential and avoid sharing them.
- **HTTPS Only:** All API requests must be made over HTTPS; HTTP requests will fail.
- **Test Environment:** Requests made in the test environment will not interact with banking networks and incur no charges.
