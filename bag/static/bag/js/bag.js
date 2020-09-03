
/* Increment item quantity */
$(".increment-qty").click(function () {
    console.log("increment");
    let quantity = $(this).closest($(".form-group")).find(".qty_input");
    let value = quantity.val();
    if (value >= 99) {
        return;
    }

    $(quantity).val(++value);

})

/* Decrement item quantity */
$(".decrement-qty").click(function () {
    console.log("decrement");
    let quantity = $(this).closest($(".form-group")).find(".qty_input");
    let value = quantity.val();
    if (value < 2) {
        return;
    }

    $(quantity).val(--value);

})

// Update quantity on click
$('.update-link').click(function () {
    allow_quantity();
    this.parentElement.getElementsByTagName('form')[0].submit();
})

function allow_quantity() {
    $(".qty_input").prop('disabled', false);
}