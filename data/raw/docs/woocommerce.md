---
url: https://docs.xendit.co/docs/woocommerce
title: WooCommerce
description: ''
section: docs
scraped_at: '2026-04-23T06:16:49.972336Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsPlug-ins
- Documentation
- Accept payments
- Plug-ins
---
# WooCommerce

WooCommerce is a WordPress plugin that turns a WordPress site into a fully functional eCommerce platform. The plugin is hosted and managed entirely by merchants within their chosen environment.

To enhance the payment experience, our **Xendit-WooCommerce plugin** can be installed on your WooCommerce store to provide secure online payment capabilities. This plugin will allow you to accept a wide range of payment methods through Xendit with minimal configuration effort.

Follow this guideline to start integrating Xendit with your WooCommerce platform.

## Requirements

Before integrating Xendit with WooCommerce, ensure the following requirements are met:

1. **System Requirements**:

   - WordPress version: **4.8.3** or above.
   - WooCommerce version: **3.1.2** or above.
   - PHP version: **7.0** or above.
   - Ensure **cURL with OpenSSL** is enabled by your web hosting provider.
2. **Xendit Account Setup**:

   - Register for a Xendit account and retrieve your **test** and **live API keys**.
   - Remove any IP whitelist from your Xendit dashboard.
   - Have **Admin** or **Developer** access in the Xendit Dashboard.
   - You do **not** need to set up a callback URL in the Xendit dashboard; the WooCommerce plugin automatically handles this.
3. **Plugin Installation**:

   - Download and install the Xendit WooCommerce plugin [here](/docs/woocommerce#).

By completing these steps, you’ll be ready to integrate and start accepting payments with Xendit on your WooCommerce store.

## Installation

1. Go to your WordPress dashboard and go to “Plugins” tab and click on “Add New”.
2. Type “WooCommerce - Xendit” on the search bar.
3. Install the plugin.
4. Go to “Installed Plugins”.
5. Activate WooCommerce - Xendit plugin and click on Settings

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/A-Oauth-5_qr0yul.jpeg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=qdHZM3eyEgJCICAkOYefejvE%2FzZg9yTFiScrXq2P6Ic%3D)
6. Click on the “Connect to Xendit” button

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/A-Oauth-6_owbwfb.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=qdHZM3eyEgJCICAkOYefejvE%2FzZg9yTFiScrXq2P6Ic%3D)
7. Make sure you’re logged in to the right Xendit account, then click on the “Allow” button

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/A-Oauth-7_dmdr4k.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=qdHZM3eyEgJCICAkOYefejvE%2FzZg9yTFiScrXq2P6Ic%3D)
8. You will be redirected to a success page in Xendit Dashboard

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/A-Oauth-8_dl1aig.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=qdHZM3eyEgJCICAkOYefejvE%2FzZg9yTFiScrXq2P6Ic%3D)
9. You may reload the Settings page on your WordPress dashboard. If you want to use Test Mode first, you can tick the “Enable Test Mode” checkbox. If you want to use Live Mode, please do otherwise. Don’t forget to click “Save Changes” in the bottom of the page

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/A-Oauth-9_lxsqqi.jpg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=qdHZM3eyEgJCICAkOYefejvE%2FzZg9yTFiScrXq2P6Ic%3D)

**If you have trouble with the installation using “Connect to Xendit” button, please follow this workaround:**

1. Instead of clicking “Connect to Xendit” button, hover to the remarks below and click the link attached to integrate using API keys

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/B-API_key-1_mlizwo.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=qdHZM3eyEgJCICAkOYefejvE%2FzZg9yTFiScrXq2P6Ic%3D)

2. You will be redirected to this page, where you can enter your API keys. Click the attached link in the image below to find your Public and Secret API keys from Xendit

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/B-API_key-2_pol75l.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=qdHZM3eyEgJCICAkOYefejvE%2FzZg9yTFiScrXq2P6Ic%3D)
3. Copy the Xendit public API key & secret API key
4. Paste it in your WooCommerce settings.
5. Click “Save Changes” on the bottom of the page

**Here are some ways to check whether your installation is successful or not:**

1. In the WooCommerce-Xendit settings page, you will see “Connected” button is grayed-out, and “Disconnect” button is available to be clicked

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/C-Check-1_ervb60.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=qdHZM3eyEgJCICAkOYefejvE%2FzZg9yTFiScrXq2P6Ic%3D)
2. When you test checkout, you can already see Xendit Payment Gateway option on the checkout page

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/New WooCommerce Checkout.jpg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=qdHZM3eyEgJCICAkOYefejvE%2FzZg9yTFiScrXq2P6Ic%3D)

## Payment flow

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screen Recording 2025-10-13 at 12.59.37.mov.gif?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A46Z&se=2026-04-23T06%3A28%3A46Z&sr=c&sp=r&sig=qdHZM3eyEgJCICAkOYefejvE%2FzZg9yTFiScrXq2P6Ic%3D)

\
