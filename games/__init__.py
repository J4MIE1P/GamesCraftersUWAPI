from .models import Game, GameVariant
from .gamesman_classic import GamesmanClassicDataProvider
from .chess import RegularChessVariant


games = {

    'ttt': Game(
        name='Tic-Tac-Toe',
        desc='Place your piece onto an open square. Wins when you connect three in a row horizontally, vertically, or diagonally',
        variants={
            'regular': GameVariant(
                name='Regular',
                desc='Regular',
                data_provider=GamesmanClassicDataProvider,
                data_provider_game_id='ttt',
                data_provider_variant_id=-1)
        }),

    'chess': Game(
        name='Chess',
        desc='Chess',
        variants={
            '7-man': RegularChessVariant()
        }),

    '1210': Game(
        name='0 to 10 by 1 or 2',
        desc='A player may either place 1 or 2 pieces on their turn. Wins when player reaches 10',
        variants={
            'regular': GameVariant(
                name='Regular',
                desc='Regular',
                data_provider=GamesmanClassicDataProvider,
                data_provider_game_id='1210',
                data_provider_variant_id=-1)
        }),

    'sim': Game(
        name='Sim',
        desc='Connect two dots with a line of your color. Wins when you force your opponent to complete a triangle',
        variants={
            'regular': GameVariant(
                name='Regular',
                desc='Regular',
                data_provider=GamesmanClassicDataProvider,
                data_provider_game_id='sim',
                data_provider_variant_id=-1)
        }),

    'ooe': Game(
        name='Odd or Even',
        desc='15 matches, take 1, 2, or 3 matches. Wins when you have even number of matches when 0 matches on board',
        variants={
            'regular': GameVariant(
                name='Regular',
                desc='Regular',
                data_provider=GamesmanClassicDataProvider,
                data_provider_game_id='ooe',
                data_provider_variant_id=-1)
        }),

    'snake': Game(
        name='Snake',
        desc='Move one step up, left, or right. Wins when your opponent has no more moves given the current position',
        variants={
            'regular': GameVariant(
                name='Regular',
                desc='Regular',
                data_provider=GamesmanClassicDataProvider,
                data_provider_game_id='snake',
                data_provider_variant_id=-1)
        }),

    'foxes': Game(
        name='Foxes & Geese',
        desc='Initially set up with seventeen geese G and one fox F. First player G, second player F. ' +
             'Players take turns moving a goose or fox to an adjacent spot. ' +
             'Geese are allowed to move one square left, right or down, ' +
             'while the fox can move either left, right, up, or down. ' +
             'The fox may also capture a goose on his turn by jumping over the goose that is in his immediate path.',
        variants={
            'regular': GameVariant(
                name='Regular',
                desc='Regular',
                data_provider=GamesmanClassicDataProvider,
                data_provider_game_id='foxes',
                data_provider_variant_id=-1)
        }),

    'dnb': Game(
        name='Dots & Boxes',
        desc='Players take turns connecting horizontal or vertical lines between dots. ' +
             'Box has a designated owner once four sides have been connected. ' +
             'Wins when a player has the majority of the boxes',
        variants={
            'regular': GameVariant(
                name='Regular',
                desc='Regular',
                data_provider=GamesmanClassicDataProvider,
                data_provider_game_id='dnb',
                data_provider_variant_id=-1)
        }),

    'tilechess': Game(
        name='Tile Chess',
        desc='A chess variant (with slightly different valid moves). Wins when checkmate opponents King',
        variants={
            'regular': GameVariant(
                name='Regular',
                desc='Regular',
                data_provider=GamesmanClassicDataProvider,
                data_provider_game_id='tilechess',
                data_provider_variant_id=-1)
        }),

    '1ton': Game(
        name='1 to n',
        desc='A player may either place 1 or 2 pieces on their turn. ' +
             'Wins when player reaches n (n is chosen by the players)',
        variants={
            'regular': GameVariant(
                name='Regular',
                desc='Regular',
                data_provider=GamesmanClassicDataProvider,
                data_provider_game_id='1ton',
                data_provider_variant_id=-1)
        })

}
