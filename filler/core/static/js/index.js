$(document).ready(function()
{
    can_move = true;
    $(document).on("click", ".option-tile.valid", function()
    {
        color = $(this).data("color");
        if(can_move)
        {
            $.ajax(
            {
                type: "POST",
                data: { color: color },
                url: "/make-move",
                success: async function(response)
                {
                    $("#game-container").html(response);
                    can_move = false;

                    await delay(2000);
                    aiMakeMove();
                }
            });
        }
    });
});

const delay = ms => new Promise(res => setTimeout(res, ms));

function aiMakeMove()
{
    $.ajax(
    {
        type: "GET",
        url: "/ai-make-move",
        success: async function(response)
        {
            $("#game-container").html(response);
            can_move = true;
        }
    });
}