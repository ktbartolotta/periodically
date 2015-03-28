define(["knockout"], function (ko) {

    function PeriodicsCompViewModel(params) {
        var self = this;

        self.resp = params.resp;
        self.periodics = ko.observableArray(
            $.each(self.resp.periodics, function(per) {
                return $.map(per, function(p) {
                    return new ElementModel(
                        p.atomic_no,
                        p.atomic_wt,
                        p.name,
                        p.symbol
                    );
                });
            })
        );
    };

    return PeriodicsCompViewModel;

});