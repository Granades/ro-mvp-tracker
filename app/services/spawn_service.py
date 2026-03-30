from datetime import datetime, timezone

from models.spawn_model import Spawn
from models.mvp_model import MVP


def close_active_spawns(spawn_reports_collection, mvp_id: str) -> int:
    result = spawn_reports_collection.update_many(
        {
            "mvp_id": mvp_id,
            "status": "active"
        },
        {
            "$set": {
                "status": "closed",
                "closed_at": datetime.now(timezone.utc),
                "closed_reason": "replaced_by_new_kill"
            }
        }
    )
    return result.modified_count


def build_spawn_from_mvp(mvp: MVP, mvp_id: str, killed_at: datetime) -> Spawn:
    return Spawn(
        mvp_id=mvp_id,
        mvp_name=mvp.name,
        map_name=mvp.map,
        killed_at=killed_at,
        respawn_min=mvp.respawn_min,
        respawn_max=mvp.respawn_max,
        status="active"
    )


def build_spawn_document(spawn: Spawn, x: int, y: int) -> dict:
    spawn_data = spawn.to_dict()
    spawn_data["tomb"] = {"x": x, "y": y}
    spawn_data["next_spawn_min"] = spawn.next_spawn_min()
    spawn_data["next_spawn_max"] = spawn.next_spawn_max()
    spawn_data["alerts_sent"] = {
        "window_open": False,
        "spawn_due": False
    }
    return spawn_data


def create_spawn_for_kill(
    spawn_reports_collection,
    mvp: MVP,
    mvp_id: str,
    x: int,
    y: int
) -> dict:
    killed_at = datetime.now(timezone.utc)

    close_active_spawns(spawn_reports_collection, mvp_id)

    spawn = build_spawn_from_mvp(
        mvp=mvp,
        mvp_id=mvp_id,
        killed_at=killed_at
    )

    spawn_data = build_spawn_document(spawn, x, y)
    spawn_reports_collection.insert_one(spawn_data)

    return spawn_data

def get_latest_active_spawn(spawn_reports_collection, mvp_id: str):
    return spawn_reports_collection.find_one(
        {
            "mvp_id": mvp_id,
            "status": "active"
        },
        sort=[("killed_at", -1)]
    )