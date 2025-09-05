from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


class TestAllRounderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        stat_current = Statistic(sp_atk=100, sp_def=100)
        stat_max = Statistic()
        mew = AllRounderPokemon(stat_max, stat_current, level=50, name="Mew", type_pk="Psychic")

        # WHEN
        multiplier = mew.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])