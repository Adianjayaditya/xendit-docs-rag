---
url: https://docs.xendit.co/docs/create-sub-accounts
title: Create sub-accounts
description: ''
section: docs
scraped_at: '2026-04-23T06:17:34.835728Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatformSet up sub-accounts
- Documentation
- xenPlatform
- Set up sub-accounts
---
# Create sub-accounts

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/xenplatform-step-1.webp?sv=2022-11-02&spr=https&st=2026-04-23T06%3A17%3A31Z&se=2026-04-23T06%3A29%3A31Z&sr=c&sp=r&sig=07AZIEbi592qzYm4AxgkPt8BSsgM0HnaM3ig3eit9JU%3D)

You can create sub-accounts using two methods:

- **Via your dashboard:** Best if you manually onboard each merchant.
- **Via API:** Best if you want to automate your merchant onboarding.

> Global accounts
>
> If you have set up a Global account and have xenPlatform activated, please [follow this guide](https://docs.xendit.co/xenplatform-global-accounts-setup) instead. This guide only apply if:
>
> - You are incorporated in Indonesia, Philippines, Malaysia, Thailand or Vietnam
> - or if you are using the [Create Account API (V2)](https://docs.xendit.co/apidocs/create-account) as a developer

## How to create sub-accounts via dashboard

Go to the `Accounts` tab and click `+Add an account`, then select a [sub-account type](/docs/sub-accounts).

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2024-11-25 at 17.29.45.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A17%3A31Z&se=2026-04-23T06%3A29%3A31Z&sr=c&sp=r&sig=07AZIEbi592qzYm4AxgkPt8BSsgM0HnaM3ig3eit9JU%3D)

If you select a **Managed** account, there are two different options to invite your merchants to sign up:

- Send invitation: We’ll send a unique link to the email entered to invite them to sign up.
- Copy unique link: You can copy and share this unique link to your merchants, which will lead to the same sign up page. Upon registration, their account will be created as a sub-account under your Master account.

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2024-11-25 at 17.34.21.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A17%3A31Z&se=2026-04-23T06%3A29%3A31Z&sr=c&sp=r&sig=07AZIEbi592qzYm4AxgkPt8BSsgM0HnaM3ig3eit9JU%3D)

## Creating sub-accounts via API

You can create sub-accounts via API and define its type in the request body. It is mandatory to provide the following parameters:

- `business_name`: To identify your sub-account. The business name you set will be the name shown to customers paying to your merchants using payment links.
- `business_email`: The email address associated with the sub-account.

  - You may reuse email addresses for Owned sub-accounts
  - Xendit sends an invitation email only for Managed sub-accounts. Owned sub-accounts still require email addresses but will not receive any emails upon creation.

Copy

Shell Session

```
curl --request POST \ --url https://api.xendit.co/v2/accounts \ --data '{"account_email":"user@example.com","type":"OWNED","public_profile":{"business_name":"Merchant1"}}'
```

Shell Session

Copy

Once your accounts have been created, you’ll be able to view them on the xenPlatform Accounts page.

## Webhook configurations

Events in your sub-account are sent to different webhook URLs based on the sub-account’s type.

- **Owned**: Sent to the master account’s webhook configurations. However, note that the webhook settings are only synchronized during the account creation. Any changes to the master account’s webhook configurations after a sub-account is created will not automatically apply to the Owned sub-accounts. Please [contact us](mailto:help@xendit.co) when you are updating webhook configurations so that we can synchronize the configurations for you.
- **Managed**: Sent to the sub-account’s webhook configurations, which can be set in the sub-account’s dashboard or using the [Set Webhook URL API](/apidocs/set-webhook-url).

## Testing

Sub-accounts can be created while your master account is still in [Test Mode](/docs/your-dashboard). Test sub-accounts allow you to create mock transactions using your test API key and see the transactions appear on your dashboard in Test Mode. You can delete sub-accounts on your dashboard only in Test mode.
