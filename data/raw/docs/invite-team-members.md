---
url: https://docs.xendit.co/docs/invite-team-members
title: Invite team members
description: ''
section: docs
scraped_at: '2026-04-23T06:19:18.786733Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatformSet up sub-accounts
- Documentation
- xenPlatform
- Set up sub-accounts
---
# Invite team members

With xenPlatform activated, you can invite your team members to access your sub-accounts’ dashboards. A common use case is to grant users on the Platform accounts access to sub-accounts as well. Only members with the Admin permission have access to this feature.

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/pum-team-members-demo_hehetr.webp?sv=2022-11-02&spr=https&st=2026-04-23T06%3A19%3A15Z&se=2026-04-23T06%3A30%3A15Z&sr=c&sp=r&sig=zb1L6pT601MwVDHLu0NaGDl0bFy%2Bl8QlPV9mWDTdzOQ%3D)

All of your team members that have access to your platform account or any of the accounts you have created will be visible in this Team Members page.

## Inviting a new team member

1. Click **Add Member** on the top-right corner of the Team Members page.
2. Enter the **email address** of the team member you want to invite, then click `Next`
3. Select the **account** you want this team member to get access to
4. Select the **permissions** that this team member will have for the chosen account

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/pum-tutorial-1_h4szu1.gif?sv=2022-11-02&spr=https&st=2026-04-23T06%3A19%3A15Z&se=2026-04-23T06%3A30%3A15Z&sr=c&sp=r&sig=zb1L6pT601MwVDHLu0NaGDl0bFy%2Bl8QlPV9mWDTdzOQ%3D)

Alternatively, you can invite a team member to your accounts from the xenPlatform accounts page:

1. Find the account you want the team member to access
2. Click on the options button on the right, and select `Add member`

## Editing user access and permissions

From the Team Members page, you can click on the Edit button for any existing team member. From this team member details page, you can:

- Invite your team members to more accounts
- Edit your team member’s permissions on each account
- Remove their access to each account

## Permissions available for sub-account users

| **Permissio**n | Managed | Owned |
| --- | --- | --- |
| View | ✅ | ✅ |
| Edit | ✅ | ✅ |
| Approve | ✅ | ✅ |
| Admin | ✅ | ✅ |
| Developer | ✅ | ❌ |
| Withdraw | ✅ | ✅ |
| No balance | ✅ | ✅ |

The Developer permission is not available for Owned accounts, hence these accounts will not be able to generate their own API keys or set their own callbacks. The Platform can use their API keys instead to set callbacks for Owned accounts via API.
