odoo.define('blog.EmployeePosAccess', function(require) {
'use strict';

const PosComponent = require('point_of_sale.PosComponent');
const ProductScreen = require('point_of_sale.ProductScreen');
const { useListener } = require("@web/core/utils/hooks");
var { PosGlobalState } = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');
const { Gui } = require('point_of_sale.Gui');
 const PosEmployee = (PosGlobalState) => class PosEmployee extends PosGlobalState {
//@override
async _processData(loadedData) {

await super._processData(loadedData);

this.hr_employee = loadedData['hr.employee'];

}
}
Registries.Model.extend(PosGlobalState, PosEmployee);

class EmployeePosAccess extends PosComponent {

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

EmployeePosAccess.template = 'EmployeePosAccess';
ProductScreen.addControlButton({

component: EmployeePosAccess,

condition: function() {

return this.env.pos;

},
});
Registries.Component.add(EmployeePosAccess);
return EmployeePosAccess;
});

