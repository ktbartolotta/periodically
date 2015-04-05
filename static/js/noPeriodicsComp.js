define(
    ["knockout", "jquery", "suggestionModel"], 
    function (ko, $, SuggestionModel) {

        function NoPeriodicsCompViewModel (params) {
            var self = this;

            self.suggestions = params.resp.no_periodics.suggestions;
            self.words = ko.observableArray(
                $.map(self.suggestions, function (s) {
                    return new SuggestionModel (s);
                })
            );
        };

        return NoPeriodicsCompViewModel;

});