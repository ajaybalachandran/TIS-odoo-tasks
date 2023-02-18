odoo.define('pos_advanced.ReturnReasonButton', function (require) {
   'use strict';
  const { Gui } = require('point_of_sale.Gui');
  const PosComponent = require('point_of_sale.PosComponent');
  const { identifyError } = require('point_of_sale.utils');
  const ProductScreen = require('point_of_sale.ProductScreen');
  const { useListener } = require("@web/core/utils/hooks");
  const Registries = require('point_of_sale.Registries');
  const PaymentScreen = require('point_of_sale.PaymentScreen');
  class ReturnReasonButton extends PosComponent {
      display_popup_return_reasons() {
      var core = require('web.core');
      var _t = core._t;
       Gui.showPopup("ReturnReasonsPopup", {
       title : _t("Return Reasons"),
       confirmText: _t("Exit")
          });
      }
   }
  ReturnReasonButton.template = 'ReturnReasonButton';
  ProductScreen.addControlButton({
      component: ReturnReasonButton,
      condition: function() {
          return true;
      },
  });
  Registries.Component.add(ReturnReasonButton);
  return ReturnReasonButton;
});



//odoo.define('pos_advanced.ReturnReasonButton', function (require) {
//    'use strict';
//    console.log('kkkkkkkkkkkkkkkkkkkkkkk')
//    // require pos screens.
//    var pos_screens = require('point_of_sale.Gui');
//    // create a new button by extending the base ActionButtonwidget
//    var DashboardButton = pos_screens.ActionButtonWidget.extend({
//        template: "DashBoardButton",
//        button_click: function(){
//        alert("Dashboard button clicked");
//        },
//    });
//    // define the dashboard button
//    pos_screens.define_action_button({
//    'name': "Dashboard",
//    'widget': DashboardButton,
//    'condition': function(){return this.pos;},
//    });
//});
