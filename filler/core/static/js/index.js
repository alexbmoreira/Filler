$(document).ready(function()
{
    $(".option-tile.valid").click(function()
    {
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