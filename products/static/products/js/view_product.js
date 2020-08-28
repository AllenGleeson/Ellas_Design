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

$(function () {
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajaxSetup({
        headers: { "X-CSRFToken": csrfToken }
    });
});

$(".deleteItem").click(function () {
    let product_id = $(this).data("id");
    
    alertify.confirm("Are you sure you want to delete this product?.",
        function () {
            $.ajax({
                method: 'DELETE',
                url: '../delete/' + product_id,
                success: function (data) {
                    //this gets called when server returns an OK response
                    window.location.href = "../";
                },
                error: function (data) {
                    alertify.error('Request failed:', data);
                }
            });
            
        },
        function () {
        });
})