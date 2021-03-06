$(function() {
    register = 'register';
    deregister = 'deregister';
    register_selector = '.' + register;
    deregister_selector = '.' + deregister;

    $(register_selector + ', ' + deregister_selector).on('click', function() {
        type_register = $(this).hasClass(register);
        type_deregister = $(this).hasClass(deregister);
        if (type_register) { type = 'register'; }
        else { type = 'deregister'; }

        if (type_register || (type_deregister && confirm('Do you want to deregister from this event?'))) {
            $.ajax({
                type: 'POST',
                url: $(this).attr('data-event-registration-url'),
                data: {
                    'type': type,
                    'csrfmiddlewaretoken': CSRF_TOKEN,
                },
                success: (response) => {
                    if (response=='Success') {
                        if (type_register) {
                            // Class is changed to allow continuous AJAX requests without reloading since ID is used for $type
                            $(this).removeClass(register).addClass(deregister);
                            $(this).removeClass('btn-success').addClass('btn-secondary');
                            $(this).html('Deregister');
                        }
                        else {
                            $(this).removeClass(deregister).addClass(register);
                            $(this).removeClass('btn-secondary').addClass('btn-success');
                            $(this).html('Register');
                        }
                        // "Number of Registered/Seats left" number is changed based on the text set by custom templatetag in events_tag.py under seats_left().
                        $selector = $(this).siblings('.occupancy');
                        text = $selector.html();
                        number = parseInt(text.match(/\d+/));
                        change = (type_register) ? -1 : 1;
                        if (text.indexOf('seats left') >= 0) {
                            $selector.html(text.replace(/\d+/, String(number + change)));
                        }
                    }
                    else if (response=='Full') {
                        alert('Sorry, we have reached full capacity for this event. Please read the event description for possible registration at the venue.');
                    }
                    else {
                        alert(response);
                        alert('Error1');
                    }
                },
                error: () => {
                    alert('Error0');
                },
            });
        }
    });
});
