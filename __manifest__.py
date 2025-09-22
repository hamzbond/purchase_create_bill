{
    'name': 'Purchase Create Vendor Bill',
    'version': '19.0.1.0.0',
    'sequence': 100,
    'summary': 'Restore Create Vendor Bill functionality with smart purchase method detection',
    'description': '''
Purchase Create Vendor Bill - Smart Billing Solution
=====================================================

🚀 **Restore Classic "Create Vendor Bill" in Odoo 19**

In Odoo 19, the traditional "Create Vendor Bill" button was replaced with an "Upload Bill" feature. 
This module restores the classic functionality with enhanced intelligence that respects different purchase methods.

✨ **Key Features:**
-------------------
🎯 **Smart Purchase Method Detection**
   • Purchase Method = "Purchase": Bills created immediately 
   • Purchase Method = "Receive": Bills created only after products received
   • Mixed Scenarios: Intelligent wizard guides the process

🧠 **Intelligent Wizard Interface**
   • Clear breakdown of ready vs. waiting items
   • Flexible options: Create partial bills or wait for all
   • User-friendly with visual feedback

🚀 **Enhanced User Experience**
   • One-click billing for simple scenarios
   • Guided workflow for complex mixed-method orders
   • Error prevention through quantity validation
   • Seamless integration with existing workflows

💼 **Perfect For:**
-------------------
✓ Service companies: Bill services immediately upon confirmation
✓ Product resellers: Bill only after receipt confirmation  
✓ Mixed operations: Handle both scenarios intelligently
✓ Compliance: Maintain proper purchase-to-pay workflows

⚡ **How It Works:**
-------------------
1. **All "Purchase" products** → One-click instant billing
2. **All "Receive" products (received)** → One-click billing for received qty
3. **Mixed scenarios** → Smart wizard appears with clear options

🔧 **Installation:**
-------------------
• Install from Apps menu - No configuration required!
• "Create Bill" button appears on confirmed purchase orders
• Works with Purchase Users and Purchase Managers

Transform your purchase-to-pay process with intelligent vendor bill creation!
    ''',
    'category': 'Purchase',
    'author': 'hamzbond',
    'website': 'https://hamzbond.github.io',
    'license': 'LGPL-3',
    'price': 0.00,
    'currency': 'USD',
    'images': [
        'static/description/banner.png',
        'static/description/screenshot_create_bill_button.png',
        'static/description/screenshot_wizard.png',
        'static/description/screenshot_vendor_bill.png',
    ],
    'depends': [
        'purchase',
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_views.xml',
        'wizards/purchase_bill_wizard_views.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'support': 'hamzbond@gmail.com',
}