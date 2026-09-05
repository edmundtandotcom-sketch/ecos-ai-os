# Edit order + beats for the Webinar Hook+Body ad. Beats are anchored to
# spoken phrases on the TIGHT timeline (see work/words_tight.txt).
OUT_NAME = "WEBINAR_THOMSON_RESERVE_9x16.mp4"

# (take, from, to) in EDIT order. Hook 1 ($3.5M budget - number + question).
# Body re-ordered: likes -> "three things making me think twice" -> dislikes.
# Retakes dropped: 144-149 (restart), 202.7-212.6 (trails off), 218 fragment.
PIECES = [
    ("hooks", 2.70, 19.00),
    ("body", 3.00, 10.10),      # I will be sharing my thoughts...
    ("body", 22.85, 25.90),     # What I like, three reasons
    ("body", 28.30, 35.50),     # One - MRT
    ("body", 38.65, 51.00),     # Two - Ai Tong
    ("body", 59.35, 66.90),     # Three - Central Catchment
    ("body", 69.10, 74.30),     # Most views are temporary
    ("body", 77.55, 81.10),     # Nobody is ever building in front of this one
    ("body", 13.10, 17.75),     # three things causing me to think twice
    ("body", 82.55, 85.20),     # What I don't like
    ("body", 86.40, 99.60),     # first - 1,268 units
    ("body", 101.20, 104.20),   # competing with your direct neighbours
    ("body", 107.00, 113.00),   # Second - after the MRT story
    ("body", 114.40, 143.30),   # prices within 800m ... $3.24 million
    ("body", 156.60, 184.10),   # highest average quantum ... proving
    ("body", 200.00, 202.00),   # Thomson Reserve review is in October,
    ("body", 202.25, 203.30),   # so I'm running
    ("body", 224.30, 278.60),   # a live webinar session ... join me live.
]

GREEN = (84, 232, 120)
RED = (214, 32, 32)

SPEC = dict(
    # act changes: whip-in + white flash + whoosh
    segments=["what i like about", "three things", "what i don't like", "thomson reserve review"],
    beats=[
        # ---------------- HOOK
        # the house opener: burst behind a typographic slam, then cut to camera
        dict(at="i have", dev="punch_slam", secs=1.9, vfx="burst", vfx_secs=0.9, vfx_gain=0.85, motion="whip",
             params=dict(text="$3.5 MILLION BUDGET", accent_word="$3.5")),
        dict(at="will thomson reserve", dev=None, secs=2.4, vfx="lightleak", vfx_secs=1.6, vfx_gain=1.0,
             motion="punch"),
        dict(at="i've bought new launches", dev=None, secs=2.2, photo="family_showflat_real.jpg"),
        dict(at="the tre ver", dev=None, secs=2.6, backdrop="sg_marinabay_towers.mp4", split=True),
        dict(at="net asset value", dev="stat_pop", secs=2.6, lead=-0.1, backdrop="sg_city_night.mp4",
             vfx="celebrate", vfx_secs=2.0,
             params=dict(value=7, prefix="$", suffix="M", decimals=0, label="PROPERTY NET ASSET VALUE",
                         sub="built from new launches")),
        dict(at="my own next property", dev=None, secs=2.0, photo="edmund_daughter_floorplan.jpg"),
        # ---------------- BODY OPEN
        dict(at="what i like and dislike", dev="split_labels", secs=2.4, lead=-0.1,
             backdrops=("cityscape.mp4", "hdb_apartments.mp4"),
             params=dict(left="LIKE", right="DISLIKE", colours=(GREEN, RED))),
        dict(at="live 60 minutes", dev="lower_ticker", secs=2.2, lead=-0.1,
             params=dict(text="LIVE 60-MIN WEBINAR")),
        # ---------------- LIKES
        dict(at="what i like about", dev="black_type_open", secs=2.3, lead=-0.05, nocap=True,
             params=dict(lines=("WHAT I LIKE", "3 REASONS"), boxed="LIKE", box_colour=GREEN)),
        dict(at="two minutes sheltered", dev="stat_pop", secs=3.0, lead=-0.1, backdrop="sg_orchard_crossing.mp4",
             params=dict(value=2, suffix=" MIN", decimals=0, label="SHELTERED WALK",
                         sub="to Upper Thomson Exit 2")),
        dict(at="ai tong school", dev=None, secs=2.4, backdrop="family_sofa.mp4", split=True),
        dict(at="oversubscribed", dev="checklist", secs=3.2, lead=-0.1, backdrop="family_kitchen.mp4",
             params=dict(title="Ai Tong School",
                         items=["WITHIN 1KM", "PHASE 2C PRIORITY", "OVERSUBSCRIBED EVERY YEAR"],
                         stagger=0.55)),
        dict(at="you can only buy", dev="accum_caption", secs=2.0, lead=-0.05,
             params=dict(words=["YOU", "CAN", "ONLY", "BUY", "INTO", "IT"], highlight=3, colour_idx=2)),
        dict(at="over 2,000 hectares", dev="stat_pop", secs=2.8, lead=-0.1, backdrop="sg_gardens_bay.mp4",
             params=dict(value=2000, suffix=" HA", decimals=0, label="OF FOREST",
                         sub="20km of trails at the door")),
        dict(at="somebody eventually builds", dev=None, secs=2.8, backdrop="sg_aerial.mp4", split=True),
        dict(at="nobody is ever", dev="accum_caption", secs=2.8, lead=-0.05, vfx="lightleak", vfx_secs=1.4,
             vfx_gain=0.7, motion="punch",
             params=dict(words=["NOBODY", "IS", "EVER", "BUILDING", "IN", "FRONT", "OF", "THIS", "ONE"],
                         highlight=0, colour_idx=0, y_frac=0.62, size=84)),
        # ---------------- DISLIKES
        dict(at="three things", dev=None, secs=1.6, vfx="glitch", vfx_secs=1.0, vfx_gain=0.8, motion="whip"),
        dict(at="what i don't like", dev="black_type_open", secs=2.2, lead=-0.05, nocap=True,
             params=dict(lines=("WHAT I", "DON'T LIKE"), boxed="DON'T", box_colour=RED)),
        dict(at="first, there are", dev=None, secs=2.4, treat="red", motion="punch"),
        dict(at="84%", dev="stat_pop", secs=3.0, lead=-0.15, backdrop="skyline_dusk.mp4",
             params=dict(value=84, suffix="%", decimals=0, label="OF 1,268 UNITS",
                         sub="in one single collection")),
        dict(at="your direct neighbours", dev="icon_compare", secs=2.4, lead=-0.1,
             params=dict(left=("DISTRICT 20", "house"), right=("YOUR NEIGHBOURS", "house"))),
        dict(at="after the thomson mrt", dev=None, secs=2.8, backdrop="sg_road_night.mp4", split=True),
        dict(at="within 800m", dev=None, secs=2.4, backdrop="sg_sunrise_traffic.mp4", split=True),
        dict(at="up 20.86", dev="stat_pop", secs=3.2, lead=-0.1, backdrop="desk_calculator_maths.mp4",
             params=dict(value=20.86, suffix="%", decimals=2, label="IN 4 YEARS",
                         sub="while the line was built")),
        dict(at="after it opened", dev="versus_bars", secs=4.2, lead=-0.1, backdrop="downtown.mp4",
             params=dict(left=("BUILDING", 20.86), right=("OPENED", 5.87),
                         title="PRICES WITHIN 800M OF TEL", unit="%")),
        dict(at="third, the price", dev=None, secs=1.4, vfx="glitch", vfx_secs=0.8, motion="punch"),
        dict(at="$2,800 to $3,000", dev="cost_stack", secs=4.0, lead=-0.1, backdrop="desk_realestate_home.mp4",
             params=dict(items=["$2,800 - $3,000 PSF", "ESTIMATE ONLY", "NOTHING OFFICIAL YET"],
                         total_label="3-bed premium lands at")),
        dict(at="$3.24 million", dev="stat_pop", secs=2.2, lead=-0.1, backdrop="sg_skyline2.mp4",
             vfx="burst", vfx_secs=0.8,
             params=dict(value=3.24, prefix="$", suffix="M", decimals=2, label="3-BEDROOM PREMIUM",
                         sub="estimated quantum")),
        dict(at="near an mrt", dev="checklist", secs=3.6, lead=-0.1, backdrop="sg_old_building.mp4",
             params=dict(title="District 20 resale 3-bed",
                         items=["NEAR AN MRT", "NEAR A TOP PRIMARY SCHOOL", "UNDER 10 YEARS OLD"],
                         stagger=0.7)),
        dict(at="from $2.7 million", dev="grid_paper_plate", secs=3.4, lead=-0.1,
             params=dict(headline="DISTRICT 20 RESALE", price_from=2.70, price_to=2.80,
                         price_labels=("3-bed resale from", "to over"),
                         lines=("what the district is transacting today",), red_word="today")),
        dict(at="half a million more", dev="dread_plate", secs=3.6, lead=-0.5,
             params=dict(numbers=(0, 250000, 500000),
                         captions=("you'll be paying", "more than", "half a million more"),
                         final_label="ABOVE DISTRICT 20 AVERAGE")),
        # ---------------- CTA
        dict(at="thomson reserve review", dev=None, secs=1.8, vfx="transition", vfx_secs=0.5, vfx_gain=0.8, motion="whip"),
        dict(at="live webinar session", dev=None, secs=2.6, backdrop="desk_laptop_typing.mp4", split=True),
        dict(at="as my next property", dev=None, secs=2.0, photo="family_showflat_model_a.png"),
        dict(at="the exact price", dev="checklist", secs=5.6, lead=-0.1, backdrop="sg_flyer_wheel.mp4",
             params=dict(title="Inside the webinar",
                         items=["THE EXACT PRICE I WALK AWAY AT", "WHICH STACKS I GO FOR",
                                "WHICH I WON'T TOUCH AT ANY PRICE"], stagger=1.6)),
        dict(at="before, during and after", dev=None, secs=2.4, backdrop="desk_calendar_calc.mp4", split=True),
        dict(at="second property at all", dev="icon_compare", secs=3.0, lead=-0.1,
             params=dict(left=("2ND PROPERTY", "house"), right=("OWN STAY", "house"))),
        dict(at="pressure-test", dev="accum_caption", secs=2.6, lead=-0.3, vfx="lightleak", vfx_secs=1.4,
             vfx_gain=0.75,
             params=dict(words=["PRESSURE-TEST", "IT", "WITH", "ME", "BEFORE", "THE", "PREVIEW"],
                         highlight=4, colour_idx=1, y_frac=0.62, size=84)),
        dict(at="click the link", dev=None, secs=3.0, frame=True, motion="punch"),
    ],
    endcard=dict(dev="black_type_open", secs=2.6,
                 params=dict(lines=("CLICK THE LINK", "JOIN ME LIVE"), boxed="LINK")),
)
