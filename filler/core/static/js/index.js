$(document).ready(function()
{
    $(document).on("click", ".option-tile.valid", function()
    {
        console.log("hello")
        color = $(this).data("color");
        $.ajax({
            type: "POST",
            data: { color: color },
            url: "/make-move",
            success: function(response)
            {
                $("#game-container").html(response);
                console.log(response);
            }
        });
    });
});