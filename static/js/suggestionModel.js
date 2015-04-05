define(["knockout", "jquery"], function (ko, $) {

    function SuggestionModel(word) {
        var self = this;

        self.word = ko.observable(word);
        self.resp = [];
        self.responseComp = ko.observable("emptyComp");
        self.wasToggled = false;
        self.isVisible = ko.observable(false);

        self.getPeriodics = function (){
            $.ajax({
                url: "/periodic/" + self.word(),
                type: "GET",
                dataType: "json",
                contentType: "application/json"
            })
            .done(function (data) {
                self.resp = data;
                self.responseComp("periodicsComp");
            })
            .fail(function (xhr, status, error) {
                console.log(status + ' ' + error);
            });
        };

        self.toggleVisible = function () {
            self.isVisible(!self.isVisible());
            if (!self.wasToggled) {
                self.wasToggled = true;
                self.getPeriodics();
            }
        };
    };

    return SuggestionModel;

});