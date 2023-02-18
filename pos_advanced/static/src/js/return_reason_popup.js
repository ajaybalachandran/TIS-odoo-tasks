odoo.define('blog.ReturnReasonsPopup', function(require) {
'use strict';

const PosComponent = require('point_of_sale.PosComponent');
const ProductScreen = require('point_of_sale.ProductScreen');
const { useListener } = require("@web/core/utils/hooks");
var { PosGlobalState } = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');
const { Gui } = require('point_of_sale.Gui');
 const ReturnReason = (PosGlobalState) => class ReturnReason extends PosGlobalState {
//@override
async _processData(loadedData) {

await super._processData(loadedData);

this.hr_employee = loadedData['hr.employee'];

}
}
Registries.Model.extend(PosGlobalState, ReturnReason);

class ReturnReasonsPopup extends PosComponent {

setup() {

super.setup();

useListener('click', this.onClick);

}


async onClick() {

console.log(this.env.pos.hr_employee,'this.env.pos.hr_employee')

var pos_employee = this.env.pos.hr_employee

for(var i=0; i < pos_employee.length; i++){

pos_employee[i]['image_url'] = window.location.origin + "/web/image/hr.employee/" + pos_employee[i].id+ "/image_1920";

}

Gui.showPopup("EmployeePos", {

title: this.env._t('Pos Employee'),

cancelText: this.env._t("Cancel"),

confirmText:this.env._t("Ok"),

pos_employee:pos_employee

});

}

}

ReturnReasonsPopup.template = 'ReturnReasonsPopup';
ProductScreen.addControlButton({

component: ReturnReasonsPopup,

condition: function() {

return this.env.pos;

},
});
Registries.Component.add(ReturnReasonsPopup);
return ReturnReasonsPopup;
});

//odoo.define('pos_advanced.ReturnReasonsPopup', function (require) {
//   'use strict';
//   const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
//   const Registries = require('point_of_sale.Registries');
//   const PosComponent = require('point_of_sale.PosComponent');
//   const ControlButtonsMixin = require('point_of_sale.ControlButtonsMixin');
//   const NumberBuffer = require('point_of_sale.NumberBuffer');
//   const { useListener } = require('web.custom_hooks');
//   const { onChangeOrder, useBarcodeReader } = require('point_of_sale.custom_hooks');
//   const { useState } = owl.hooks;
//
//
//
//
//class ReturnReasonsPopup extends AbstractAwaitablePopup {
//    constructor() {
//    super(...arguments);
//    useListener('click-product', this._clickProduct);
//    }
//   CouponProductsPopup//To get coupon products category
//    get productsToDisplay() {
//    return this.env.pos.db.get_product_by_category(this.env.pos.config.category_id[0]);
//    }
//     get currentOrder() {
//           return this.env.pos.get_order();
//       }
////      get products details in orderlines when clicking on popup product
//     async _clickProduct(event) {
//           if (!this.currentOrder) {
//               this.env.pos.add_new_order();
//           }
//
//           const product = event.detail;
//           let price_extra = 0.0;
//           let description, packLotLinesToEdit;
//           // Add the product after having the extra information.
//           this.currentOrder.add_product(product, {
//               description: description,
//           });
//       }
//    }
//    //Create products popup
//   CouponProductsPopup.template = 'ReturnReasonsPopup';
//   CouponProductsPopup.defaultProps = {
//       confirmText: 'Ok',
//       cancelText: 'Cancel',
//       title: 'Return Reasons',
//       body: '',
//   };
//   Registries.Component.add(ReturnReasonsPopup);
//   return ReturnReasonsPopup;
////   export default  ReturnReasonsPopup;
//
//
//
//});



