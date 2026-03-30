from datetime import datetime, timedelta, timezone


class Spawn:
    def __init__(
        self,
        mvp_id: str,
        mvp_name: str,
        map_name: str,
        killed_at: datetime,
        respawn_min: int,
        respawn_max: int,
        status: str = "active",
        _id=None,
    ):
        self.id = _id
        self.mvp_id = mvp_id
        self.mvp_name = mvp_name
        self.map = map_name
        self.killed_at: datetime = self._ensure_utc(killed_at)
        self.respawn_min = respawn_min
        self.respawn_max = respawn_max
        self.status = status

    @staticmethod
    def _ensure_utc(dt: datetime | None) -> datetime | None:
        if dt is None:
            return None
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    @classmethod
    def from_dict(cls, data: dict) -> "Spawn":
        return cls(
            mvp_id=data.get("mvp_id"),
            mvp_name=data.get("mvp_name"),
            map_name=data.get("map"),
            killed_at=data.get("killed_at"),
            respawn_min=data.get("respawn_min"),
            respawn_max=data.get("respawn_max"),
            status=data.get("status", "active"),
            _id=data.get("_id"),
        )

    def to_dict(self) -> dict:
        return {
            "mvp_id": self.mvp_id,
            "mvp_name": self.mvp_name,
            "map": self.map,
            "killed_at": self.killed_at,
            "respawn_min": self.respawn_min,
            "respawn_max": self.respawn_max,
            "status": self.status,
        }

    def next_spawn_min(self) -> datetime:
        return self.killed_at + timedelta(minutes=self.respawn_min)

    def next_spawn_max(self) -> datetime:
        return self.killed_at + timedelta(minutes=self.respawn_max)

    def is_window_open(self) -> bool:
        return datetime.now(timezone.utc) >= self.next_spawn_min()

    def is_overdue(self) -> bool:
        return datetime.now(timezone.utc) >= self.next_spawn_max()

    def time_until_spawn(self) -> timedelta:
        now = datetime.now(timezone.utc)
        return self.next_spawn_min() - now