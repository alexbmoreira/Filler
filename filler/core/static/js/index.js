$(document).ready(function()
{
    game_data = $("#board").data("game")
    window.localStorage.setItem('game', JSON.stringify(game_data))

    can_move = true;

    $(document).on("click", ".option-tile.valid", function()
    {
        color = $(this).data("color");
        if(can_move)
        {
            game = JSON.parse(window.localStorage.getItem('game'))
            $.ajax(
            {
                type: "POST",
                data: JSON.stringify({ color: color, game: game }),
                contentType: "application/json",
                url: "/make-move",
                success: async function(response)
                {
                    window.localStorage.removeItem('game')
                    $("#game-container").html(response);
                    window.localStorage.setItem('game', JSON.stringify($("#board").data("game")))
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
    game = JSON.parse(window.localStorage.getItem('game'))
    $.ajax(
    {
        type: "POST",
        data: JSON.stringify({ game: game }),
        contentType: "application/json",
        url: "/ai-make-move",
        success: async function(response)
        {
            window.localStorage.removeItem('game')
            $("#game-container").html(response);
            window.localStorage.setItem('game', JSON.stringify($("#board").data("game")))

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