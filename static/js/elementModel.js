define(['knockout'], function (ko) {

    function ElementModel (atomic_no, atomic_wt, name, symbol) {
        var self = this;

        self.atomic_no = ko.observable(atomic_no);
        self.atomic_wt = ko.observable(atomic_wt);
        self.name = ko.observable(name);
        self.symbol = ko.observable(symbol);
    };

    return ElementModel;

});