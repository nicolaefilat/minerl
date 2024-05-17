from minerl.herobraine.env_specs.navigate_specs import Navigate
from minerl.herobraine.hero.handler import Handler
from minerl.herobraine.hero.handlers.agent.observations.location_stats import _XPositionObservation, _YPositionObservation, _ZPositionObservation
from typing import List

class NavigateProgSynthesis(Navigate):
    def __init__(self, dense, extreme, *args, **kwargs):
        super().__init__(dense, extreme, sfx='ProgSynth')

    def create_observables(self) -> List[Handler]:
        return super().create_observables() + [
            _XPositionObservation(),
            _YPositionObservation(),
            _ZPositionObservation()
        ]
