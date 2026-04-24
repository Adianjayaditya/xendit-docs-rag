---
url: https://docs.xendit.co/docs/plug-in-cloudbeds
title: Cloudbeds
description: ''
section: docs
scraped_at: '2026-04-23T06:16:32.959339Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsPlug-ins
- Documentation
- Accept payments
- Plug-ins
---
# Cloudbeds

Cloudbeds Booking Engine is an all-in-one solution for hotels, hostels, vacation rentals, and homestays. Cloudbeds platforms provide a seamless booking experience for guests. It provides a customizable interface and a streamlined booking experience for guests, encouraging direct bookings to increase revenue.

**Important Note:** Xendit is only compatible with the Cloudbeds Booking Engine (direct website). It does not work with bookings made through Cloudbeds Channel Manager (e.g., Agoda, Traveloka, Booking.com).

### Installation guide

You can initiate the Xendit integration with Cloudbeds using two methods:

**Method 1: From Xendit Dashboard**

1. Go to your **Xendit dashboard**
2. Navigate to **Integrations** > **Cloudbeds**
3. Click **Install**

   ![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/step_1_cloudbeds_int_kxaip3.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)

**Method 2: From Cloudbeds Account**

1. Log in to your **Cloudbeds account**
2. Go to **Apps & Marketplace**
3. Search for **Xendit**
4. Click **Learn more**, then click **Connect App**

   ![Xendit payment app overview, highlighting features for accepting various payment methods.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot_2024-01-08_110015_tse7pr.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)

**Prerequisite:** Ensure your Xendit account has **Developer permissions** to perform this integration.

## How to install

1. **Grant Cloudbeds Access**

   After initiating the integration (from either method above), you will be redirected to the Cloudbeds consent page. Ensure you are logged into your Cloudbeds account, then click **Allow access**

   ![Instructions to allow access by clicking the 'Allow Access' button on the screen.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/step_2_cloudbeds_int_i7omux.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)
2. **Grant Xendit Access**

   Next, you will be redirected to the Xendit consent page. Click **Allow** to proceed. You will then be redirected back to Cloudbeds.

   ![Prompt to click 'Allow' for Cloudbeds integration access on Xendit dashboard.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/step_3_cloudbeds_int_gfmpna.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)
3. **Verify Payment Method**

   Xendit should now automatically appear under **Payments** > **Payment Options** > **Additional and Custom Payment Methods** in your Cloudbeds account.

   ![Payments section showing options to add additional payment methods for transactions.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot_2024-01-08_111604_rcwqjk.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)
4. **Configure Custom Field**

   - Go to the **Guests** tab
   - Locate `is_xendit` under **Custom Field Name** in the custom fields table.
   - Click **Edit** on the right side of the table
   - Under "Where would you like this field to display?", ensure **Internet Booking Engine** is checked

     ![Custom fields section showing the 'is_xendit' input field for guest reservations.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/step_4_cloudbeds_int_yq5l23.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)

     ![Custom fields setup for guest reservations in a booking engine interface.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot_2024-02-19_104954_jcbrjy.jpg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)
5. **Add CSS & JavaScript:**

   - Navigate to **Booking Engine** > **Customize**.
   - Copy and paste the following CSS and JavaScript code into the **Booking Engine Header**:

     HTML, XML

     ```
     <link rel="stylesheet" href="https://tpi-assets.xendit.co/cloudbeds/css/checkout.min.css" />
     <script src="https://code.jquery.com/jquery-3.7.0.min.js" integrity="sha256-2Pmvv0kuTBOenSvLm6bvfBSSHrUJ+3A7x6P5Ebd07/g=" crossorigin="anonymous"></script>
     <script src="https://tpi-assets.xendit.co/cloudbeds/js/checkout.min.js"></script>
     ```

     HTML, XML

     Copy

     ![Instructions for adding CSS/JS code to the hotel booking page header.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/step_5_cloudbeds_int_bzmrne.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)
6. **Activate Bank Transfer**

   - Go to **Payments** > **Payment Options** > **Bank Transfer**
   - Toggle the switch to **activate** this payment method

     ![Instructions for enabling bank transfer payment option in the partner account settings.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/step_6_cloudbeds_int_ogxqyg.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)
7. **Set default reservation status**

   - Go to **Property** > **Profile** > **Confirmation Pending**
   - Change "What status should direct reservations have by default?" to **Confirmation Pending**

     ![Instructions to change reservation status to Confirmation Pending in Xendit Partner Account.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot_2024-01-08_113514_wdvczp.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)

### Testing the Xendit Checkout

1. Go to **Booking Engine** > **Summary**

   ![Instructions for accessing the booking engine and social media integration options.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/step_7_cloudbeds_int_lc53e1.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)
2. Click on your **Booking Page link**
3. On the checkout page, **Online Payments via Xendit** should now be displayed under **Payment Method**

   ![Reservation page showing Xendit payment option and user contact information fields.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/step_7_2_cloudbeds_int_yqjgsq.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)
4. Click **Pay Now** to be redirected to the Xendit payment page

   ![Instructions to click 'Pay now' for Xendit invoice creation on reservation page.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/step_7_3_cloudbeds_int_zvl7c3(2).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)

## Additional Settings

#### Changing Deposit Amount

You can customize the deposit amount charged to your customers. This amount will be reflected on both the Cloudbeds and Xendit checkout pages.

- Here's how deposit amount looks like on Cloudbeds checkout page:

  ![Reservation summary showing deposit amount and payment details for Andy Nguyen's booking.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot_2024-01-08_153517_dpahfl.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)
- Here's how deposit amount looks like on Xendit checkout page:

  ![Order summary showing total amount due and payment details for a deluxe queen room.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot_2024-01-08_153551_wyiywn.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)

**How to change default deposit amount:**

1. Go to **Property Settings**

   ![Navigate to Property settings in the Xendit Partner Account interface for profile management.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Screenshot_2024-01-08_153713_m981ve.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A16%3A29Z&se=2026-04-23T06%3A28%3A29Z&sr=c&sp=r&sig=pNP00j0g5ogh17AL5NtXcgxT2Ikf37Gq1P7lKFibAB0%3D)
2. Navigate to **Policies**
3. Enter your desired deposit amount. To charge the full amount, set it to 100%.
4. Click **Save**

### Voiding Transactions in Cloudbeds

If you need to void a transaction made in error, refer to the detailed instructions on voiding transactions within Cloudbeds [here](https://myfrontdesk.cloudbeds.com/hc/en-us/articles/1260805465149-How-to-Void-Transactions#voiding-transactions-in-reservation-folio).

## Installation for Cloudbeds Booking Engine Plus (V3)

If you are using Cloudbeds Booking Engine Plus, follow the initial installation steps, and then proceed with the additional steps below:

1. **Delete Custom Field:**

   - Go to **Cloudbeds Dashboard** > **Settings** > **Guests tab** > **Custom Fields**.
   - Delete the `is_xendit` custom field from the table.
2. **Add CSS CDN:**

   - Go to **Booking Engine tab** > **Customize**.
   - Copy and paste the following CSS CDN into the **Custom Meta Tags** input:

     HTML

     Plain text

     ```
     <link rel="stylesheet" href="https://tpi-assets.xendit.co/cloudbeds/css/checkout-v3.min.css" />
     ```

     Plain text

     Copy
3. **Add JavaScript CDN:**

   - Copy and paste the following JavaScript CDN into the **Javascript** input:

     HTML

     Plain text

     ```
     <script src="https://tpi-assets.xendit.co/cloudbeds/js/checkout-v3.min.js" type="text/javascript"> </script>
     ```

     Plain text

     Copy

### Limitation

Cloudbeds Booking Engine Plus (V3) can only accept one payment method. When using Xendit with V3, ensure it is the only active payment channel option on your checkout page. Avoid using other payment provider integrations simultaneously.
