import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from model.game import Game
from services.game_service import GameService

app = FastAPI()

game_service = GameService()


@app.post("/create-game")
async def create_game(player_name: str, min_x: int, max_x: int, min_y: int,
                      max_y: int, min_z: int, max_z: int):
    return game_service.create_game(player_name, min_x, max_x, min_y, max_y,
                                    min_z, max_z)


@app.post("/join-game")
async def join_game(game_id: int, player_name: str) -> bool:
    return game_service.join_game(game_id, player_name)


@app.get("/get-game")
async def get_game(game_id: int) -> Game:
    return game_service.get_game(game_id)


@app.post("/add-vessel")
async def add_vessel(game_id: int, player_name: str, vessel_type: str, x: int,
                     y: int, z: int) -> bool:
    return game_service.add_vessel(game_id, player_name, vessel_type, x, y, z)


@app.post("/shoot-at")
async def shoot_at(game_id: int, shooter_name: str, vessel_id: int, x: int,
                   y: int, z: int) -> bool:
    return game_service.shoot_at(game_id, shooter_name, vessel_id, x, y, z)


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"{exc}"}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
