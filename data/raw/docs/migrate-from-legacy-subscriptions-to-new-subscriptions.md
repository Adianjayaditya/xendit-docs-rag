---
url: https://docs.xendit.co/docs/migrate-from-legacy-subscriptions-to-new-subscriptions
title: Migrate to New Subscription Version
description: ''
section: docs
scraped_at: '2026-04-23T06:23:07.419472Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guideSubscriptions
- Documentation
- Accept payments
- Integration guide
- Subscriptions
---
# Migrate to New Subscription Version

We introduce a new version of our subscription product. It consolidate the experiences with our Payment Sessions product for a smoother UI experience and more uniform payment experiences.

## Feature Comparison

| Feature | Legacy Subscription | New Subscription |
| --- | --- | --- |
| Payment Link and Component Support | Limited only on Payment Link | Both Payment Link and Component |
| Payment Channels Availability | Limited to legacy payment methods and specific regions | Availability for all existing channels and new channels in all regions Xendit supported |
| New design for hosted page | Old design style, payment channel categorization is outdated | Fresh new design with improvement in user experience |
| Uniform experiences on payment interfaces | Separate payment lifecycle overview on `payment_method` and UI experiences | One integration principle on each lifecycle on payment interfaces and payment object |
| Support on initial payment | Only available via legacy parameter `immediate_action_type` | Recommended to use `PAY_AND_SAVE` flow (learn more) with also backward compatibility with parameter `immediate_payment` |

> Create Subscription via Dashboard
>
> Creation and list of subscription activities will only display the legacy subscription, the new version will currently only supported via API.
>
> We will have an update in the upcoming timeline to support the new version as well.

## How to migrate

### Update your integration

### **Overall Flow**

| Conditions | Legacy Subscription | New Subscription |
| --- | --- | --- |
| **Using Xendit Hosted URL** | | |
| Create Subscription Plan | `POST /recurring/plans` with:   - empty `payment_method` - required `success_return_url` and `failure_return_url`   Response will return `actions.url` to proceed the linking process | `POST /sessions` with:   - `session_type: “SUBSCRIPTION”` to initate the session   Response will return either `payment_link_url` or `components_sdk_key` depending on your integration `MODE` |
| Using current payment token | Using legacy `payment_methods` parameter | Using current `payment_tokens` parameter |

### **Header**

| Parameters | Legacy Subscription | New Subscription |
| --- | --- | --- |
| `api-version` | `2022-10-01` | `2026-01-01` |

### Parameter Conversion

The new subscription supports most of the functionality of the legacy subscription. The following table maps the parameters and configuration differences between the two versions. Please refer to the API docs for the full lists

| Legacy Subscription | New Subscription | Notes |
| --- | --- | --- |
| `payment_methods` | `payment_tokens` | Support the new payment tokens object |
| `immediate_action_type` | `immediate_payment` | Defined as a boolean type to support immediate payment |
| `recurring_action` | - | Simplified action with only `PAYMENT` |
| `notification_config.recurring_created, notification_config.recurring_created and notification_config.recurring_failed` | `notification_channels` | Simplified into one parameter to configure the notification channel |

### Handle New Errors

Adapt on your server’s logic to handle errors in [Payment Sessions response](https://docs.xendit.co/apidocs/create-session) upon creation and [Subscriptions response](https://docs.xendit.co/apidocs/create-recurring-plan)

### Adjust and handle your webhook setup

**Legacy Subscription**

Available on the legacy webhook configuration page

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2026-04-08 at 1.50.01 AM(1).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A23%3A03Z&se=2026-04-23T06%3A34%3A03Z&sr=c&sp=r&sig=%2B6EmaNnghEjZijSPJessWP037P4bLJva05dKseVCrfY%3D)

**New Subscription**

Available on the new webhook configuration

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot 2026-04-08 at 1.50.19 AM.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A23%3A03Z&se=2026-04-23T06%3A34%3A03Z&sr=c&sp=r&sig=%2B6EmaNnghEjZijSPJessWP037P4bLJva05dKseVCrfY%3D)

#### **Optional but recommended**

Adjust the webhook URL to receive the information upon your subscription lifecycle.

**Payment v3 – Payment Status**

Xendit sends webhooks whenever there is a status update on a Payment object.

- `payment.succeeded` Identifies successful payments and includes full payment details.
- `payment.failure` Identifies failed payment attempts, including failures that occur on the Xendit hosted page.

**Payment Tokens v3 – Payment Token Status**

Xendit sends webhooks whenever there is a status update on a Payment Token object.
