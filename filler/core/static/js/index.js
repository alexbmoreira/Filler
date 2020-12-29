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
                type: "GET",
                data: { color: color },
                url: "/make-move",
                success: async function(response)
                {
                    $("#game-container").html(response);
                    can_move = false;

                    if($("#player-score").data("score") + $("#computer-score").data("score") < 64)
                    {
                        await delay(1000);
                        aiMakeMove();
                    }
                    else
                    {
                        showOutcome();
                    }
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

            if($("#player-score").data("score") + $("#computer-score").data("score") < 64)
            {
                can_move = true;
            }
            else
            {
                showOutcome();
            }
        }
    });
}

function showOutcome()
{
    if($("#player-score").data("score") < $("#computer-score").data("score"))
    {
        $("#game-over").removeClass("hidden");
        $("#outcome").addClass("loss");
        $("#outcome-text").text("You Lost!");
    }
    else if($("#player-score").data("score") > $("#computer-score").data("score"))
    {
        $("#game-over").removeClass("hidden");
        $("#outcome").addClass("win");
        $("#outcome-text").text("You Won!");
    }
    else
    {
        $("#game-over").removeClass("hidden");
        $("#outcome").addClass("draw");
        $("#outcome-text").text("Draw!");
    }
}