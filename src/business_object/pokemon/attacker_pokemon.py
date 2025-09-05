from business_object.pokemon.abstract_pokemon import PokemonAbstractPokemon


class AttackerPokemon(PokemonAbstractPokemon):
    """
    """

    def __init__(self, stat_max, stat_current, level, name, type_pk):
        super().__init__(stat_max, stat_current, level, name, type_pk)

    def get_pokemon_attack_coef(self):
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
        return 1 + (self.speed_current + self.attack_current) / 200