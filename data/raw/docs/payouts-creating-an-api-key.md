---
url: https://docs.xendit.co/docs/payouts-creating-an-api-key
title: Create an API key
description: ''
section: docs
scraped_at: '2026-04-23T06:18:24.057972Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationSend moneyIntegration setup
- Documentation
- Send money
- Integration setup
---
# Create an API key

Before you start, you need to have a Xendit account. You can create one by [signing up here](https://dashboard.xendit.co/register/1). Once that’s done, you’ll be able to start testing immediately by using your account in Test Mode.

## How to create your API key

1. Generate a Secret API Key for development [on your settings page](https://dashboard.xendit.co/settings/developers#api-keys) or by visiting **Settings** > **Developers** > **API Keys** on your dashboard
2. Make sure to set **Write** permissions for your API Key for money-in features
3. Ensure that the **API key is not given any permissions beyond the purpose it was meant for**. Doing so might lead to security incidents. See our [API key guide](/v1/docs/api-keys) here for more information
4. Store your API key securely using a secrets management solution
