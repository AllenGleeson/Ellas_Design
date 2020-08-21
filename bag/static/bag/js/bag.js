
/* Increment item quantity */
$(".increment-qty").click(function () {
    console.log("increment");
    let quantity =  $(this).closest($(".form-group")).find(".qty_input");
    let value = quantity.val();
    if (value >= 99) {
        return;
    }

    $(quantity).val(++value);

})

/* Decrement item quantity */
$(".decrement-qty").click(function () {
    console.log("decrement");
    let quantity =  $(this).closest($(".form-group")).find(".qty_input");
    let value = quantity.val();
    if (value < 2) {
        return;
    }

    $(quantity).val(--value);

})

// Update quantity on click
$('.update-link').click(function () {
    $(".update-form").submit();
})

/* // Remove item and reload on click
$('.remove-item').click(function () {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/bag/remove/${itemId}/`;
    var data = { 'csrfmiddlewaretoken': csrfToken };
    console.log(csrfToken);
    $.post(url, data)
        .done(function () {
            location.reload();
        });
}) */