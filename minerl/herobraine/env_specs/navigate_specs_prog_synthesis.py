from minerl.herobraine.env_specs.navigate_specs import Navigate
from minerl.herobraine.hero.handler import Handler
from minerl.herobraine.hero.handlers.agent.observations.location_stats import _XPositionObservation, _YPositionObservation, _ZPositionObservation
from typing import List

import minerl.herobraine.hero.handlers as handlers

class NavigateProgSynthesis(Navigate):
    def __init__(self, dense, extreme, *args, **kwargs):
        super().__init__(dense, extreme, sfx='ProgSynth')

    def create_observables(self) -> List[Handler]:
        return super().create_observables() + [
            _XPositionObservation(),
            _YPositionObservation(),
            _ZPositionObservation()
        ]
    
    def create_server_decorators(self) -> List[Handler]:
        return [handlers.NavigationDecorator(
            max_randomized_radius=64,
            min_randomized_radius=64,
            block='diamond_block',
            placement='surface',
            max_radius=8,
            min_radius=0,
            max_randomized_distance=8,
            min_randomized_distance=0,
            randomize_compass_location=False
        )]
