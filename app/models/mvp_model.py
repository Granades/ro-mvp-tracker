from datetime import datetime, timedelta


class MVP:
    def __init__(
        self,
        name: str,
        map_name: str,
        mob_id: int,
        sprite: str,
        map_image: str,
        respawn_min: int,
        respawn_max: int,
        _id=None,
    ):
        self.id = _id
        self.name = name
        self.map = map_name
        self.mob_id = mob_id
        self.sprite = sprite
        self.map_image = map_image
        self.respawn_min = respawn_min
        self.respawn_max = respawn_max

    # Crear desde Mongo (dict → objeto)
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            map_name=data.get("map"),
            mob_id=data.get("mob_id"),
            sprite=data.get("sprite"),
            map_image=data.get("map_image"),
            respawn_min=data.get("respawn_min"),
            respawn_max=data.get("respawn_max"),
            _id=data.get("_id"),
        )

    # Convertir a Mongo (objeto → dict)
    def to_dict(self):
        return {
            "name": self.name,
            "map": self.map,
            "mob_id": self.mob_id,
            "sprite": self.sprite,
            "map_image": self.map_image,
            "respawn_min": self.respawn_min,
            "respawn_max": self.respawn_max,
        }
    ##About use .gif

    def get_sprite_url(self) -> str | None:
        if not self.mob_id:
            return None
        return f"https://file5s.ratemyserver.net/mobs/{self.mob_id}.gif"



