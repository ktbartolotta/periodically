requirejs.config({

    baseUrl: "static/js",

    paths: {
        "jquery": "https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min",
        "knockout": "https://cdnjs.cloudflare.com/ajax/libs/knockout/3.3.0/knockout-min",
        "bootstrap": "https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min"
    },

    shim: {
        "bootstrap": { deps: ["jquery"] }
    }

});

requirejs(['periodics']);