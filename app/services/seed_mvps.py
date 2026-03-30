from models.mvp_model import MVP


def seed_mvps(mvps_collection):
    if mvps_collection.count_documents({}) > 0:
        print("MVPs ya existen, skipping seed")
        return

    print("Seeding MVPs...")

    mvps = [
        MVP(
            name="Maya",
            map_name="anthell02",
            mob_id=1147,
            sprite="/static/sprites/maya.gif",
            map_image="/static/maps/anthell02.gif",
            respawn_min=60,
            respawn_max=70,
        ),
        MVP(
            name="Ifrit",
            map_name="thor_v03",
            mob_id=1832,
            sprite="/static/sprites/ifrit.gif",
            map_image="/static/maps/thor_v03.gif",
            respawn_min=10,
            respawn_max=12,
        )
    ]

    mvps_collection.insert_many([mvp.to_dict() for mvp in mvps])

    print("MVPs seeded correctamente")