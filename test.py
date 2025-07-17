COUNTER = -1

def test(move):
    global COUNTER

    """
    game = ["e4", "e5", "Nf3", "Nf6", "Nc3", "Nc6", "g3", "d5", "exd5", "Nxd5", "Bg2", "Nxc3", "bxc3", "Bg4", "h3",
            "Bxf3", "Qxf3", "Qf6", "Qd5", "Rd8", "Qb3", "Na5", "Qb5+", "Nc6", "Qxb7", "a5", "Bxc6+", "Ke7", "Ba3+",
            "Ke6", "Qb3+", "Kf5", "d3", "Bxa3", "Be4+", "Kg5", "Qxa3", "Qb6", "O-O", "f5", "Qe7+", "Kg6", "Rab1", "Qd6", "Qxd6+",
            "cxd6", "Bd5", "Rc8", "c4", "h5", "Rb6", "Rhd8", "Rfb1", "Kg5", "Rb7", "g6", "h4+", "Kg4", "Kg2", "e4",
            "f3+", "exf3+", "Bxf3#"]

    game = ["e4", "c5", "c3", "Nc6", "d4", "cxd4", "cxd4", "e6", "d5", "Nb4", "a3", "Na6", "d6", "Qa5+", "Nc3",
            "Qe5", "Nb5", "Qxe4", "Be2", "Nf6", "Be3", "Qe5", "Nf3", "Qf5", "Rc1", "Nd5", "Bd3", "Qg4", "Rc4",
            "Qh5", "Qc1", "f6", "Rxc8+", "Rxc8", "Qxc8+", "Kf7", "Qxd7+", "Ne7", "dxe7", "Bxe7", "Nd6+", "Kf8", "Qc8+",
            "Bd8","Qxd8+", "Qe8", "Qxe8#"]

    game = ["c4", "Nf6", "Nc3", "e6", "Qc2", "d5", "cxd5", "exd5", "Nf3", "d4", "Nb5", "c5", "e3", "a6", "Na3",
            "dxe3", "dxe3", "b5", "Nb1", "Bb7", "a3", "Bd6", "Nc3", "O-O", "h4", "Re8", "Ng5", "Nbd7", "b3",
            "Nf8", "Bb2", "h6", "Ne2", "hxg5", "hxg5", "Ne4", "Ng3", "Nxg3", "fxg3", "Bxg3+", "Ke2", "Qxg5", "Qc3",
            "Rad8", "Rh3", "Qg4#"]

    game = ["e4", "c6", "Nf3", "d5", "exd5", "cxd5", "Bb5+", "Bd7", "Bxd7+", "Nxd7", "O-O", "e6", "d4", "Ngf6", "Bg5",
            "Bd6", "Nc3", "Qb6", "b3", "Rc8", "Na4", "Qc7", "Rc1", "O-O", "c3", "b5", "Nb2", "Ba3", "Rc2",
            "Bxb2", "Rxb2", "Qxc3", "Re2", "h6", "Bxf6", "Nxf6", "Ne5", "Ne4", "f3", "Nd6", "g4", "b4", "f4",
            "Nb5", "f5", "Nxd4", "Rd2", "Qe3+", "Kg2", "Qxe5", "Rxd4", "Rc3", "fxe6", "fxe6", "Rxf8+", "Kxf8", "Qf1+",
            "Kg8", "Rf4", "Rc2+", "Rf2", "Qe4+", "Kg1", "Qxg4+", "Kh1", "Rxf2", "Qxf2", "Qd1+", "Kg2", "Qg4+", "Kf1",
            "Qf5", "h4", "Qxf2+", "Kxf2", "Kf7", "Kf3", "a5", "Kf4", "Kf6", "h5", "e5+", "Ke3", "Kf5", "Kf3", "d4",
            "Ke2", "Kf4", "Kd3", "Kf5", "Kc4", "Ke4", "Kb5", "d3", "Kxa5", "d2", "Kxb4", "d1=Q", "Ka4", "Qd5", "b4",
            "Kd3", "a3", "Kc3", "b5", "Qc4+", "Ka5", "Qc7+", "b6", "Qb7", "a4", "e4", "Kb5", "e3", "a5", "e2", "a6",
            "Qd5+", "Ka4", "Qb3+", "Ka5", "Qb4#"]

    game = ["d4", "Nf6", "Bf4", "c5", "c3", "cxd4", "Qxd4", "Nc6", "Qd1", "d5", "Nf3", "Bf5", "e3", "e6", "Nbd2",
            "Bd6", "Ne5", "Nxe5", "Qa4+", "Qd7", "Bb5", "Nc6", "Bxd6", "Qxd6", "Nf3", "O-O", "Bxc6", "bxc6", "Nd4",
            "c5", "Nc6", "Qc7", "O-O-O", "c4", "f3", "a5", "e4", "dxe4", "fxe4", "Bxe4", "Nd4", "Rfb8", "Rhg1",
            "Qf4+", "Rd2", "Bd3", "g3", "Qh6", "Rg2", "Ne4", "Nc6", "Rb6", "Ne7+", "Kh8", "Qd7", "Rab8", "Ng6+",
            "fxg6", "b3", "Nxd2", "Rxd2", "Rf8", "Kb2", "Qxd2+", "Ka3", "Qxc3", "Qxg7+", "Kxg7", "g4", "Rxb3+", "axb3",
            "Qxb3#"]

    game = ["e4", "c6", "Nf3", "d5", "exd5", "cxd5", "d4", "Nc6", "Be2", "Nf6", "O-O", "Bg4", "Re1", "e6", "h3",
            "Bxf3", "Bxf3", "Be7", "Nc3", "O-O", "Bf4", "Qb6", "b3", "Qxd4", "Qxd4", "Nxd4", "Rac1", "Nxf3+", "gxf3",
            "Bb4", "Bd2", "Rac8", "Nb1", "Bxd2", "Nxd2", "Rc6", "c4", "dxc4", "Nxc4", "Rfc8", "Kg2", "b5", "Red1",
            "bxc4", "bxc4", "h6", "c5", "Rxc5", "Rxc5", "Rxc5", "Rd8+", "Kh7", "Ra8", "Ra5", "Rb8", "Rxa2", "Rb7",
            "Nd5", "Rxf7", "a5", "Rf8", "a4", "Re8", "Re2", "f4", "a3", "Kf3", "Nc3", "Ra8", "a2", "h4",
            "Re1", "Rxa2", "Nxa2", "h5", "Nc3", "f5", "exf5", "Kf4", "Rf1", "f3", "Nd5+", "Kxf5", "Rxf3+", "Ke4", "Rf6",
            "Kxd5", "g6", "hxg6+", "Kxg6", "Ke4", "Kg5", "Ke3", "Kg4", "Ke4", "Re6+", "Kd5", "Kf5", "Kd4", "Re7", "Kd5",
            "Rd7+", "Kc4", "Ke4", "Kc5", "Ke5", "Kc6", "Rd1", "Kc5", "Rc1", "Kb6", "Kd5", "Kb7", "Kd6", "Kb8", "Kd7",
            "Kb7", "Rb1+", "Ka6", "Kc6", "Ka5", "Kc5", "Ka4", "Kc4", "Ka3", "Kc3", "Ka2", "Rb8", "Ka1", "Kc2", "Ka2",
            "Ra8#"]

    game = ["e4", "c6", "d4", "d5", "e5", "c5", "c3", "cxd4", "cxd4", "Nc6", "Nf3", "Bg4", "Be2", "e6", "O-O",
            "Nge7", "h3", "Bxf3", "Bxf3", "Nf5", "Be3", "Qb6", "b3", "Nfxd4", "a4", "Nxf3+", "Qxf3", "Qc7", "Bf4", "Nxe5",
            "Bxe5", "Qxe5", "Na3", "Bd6", "Nb5", "Qh2#"]

    game = ["e4", "e6", "d4", "d5", "e5", "c5", "c3", "Nc6", "Nf3", "cxd4", "cxd4", "Bb4+", "Nc3", "a6", "Bd2",
            "Nge7", "a3", "Ba5", "Bd3", "Bb6", "Ne2", "O-O", "O-O", "Ba7", "Bc3", "b5", "Bc2", "Ng6", "Rc1", "Nce7",
            "Bb1", "Bb7", "Qc2", "Rc8", "Qd3", "Qd7", "Bb4", "Rxc1", "Rxc1", "Rc8", "Qd2", "Rc4", "Ba2", "Rxc1",
            "Qxc1", "Nc6", "Bc5", "Bb8", "b4", "Nce7", "Ng3", "Bc6", "h4", "Qb7", "h5", "Nf8", "Bb1", "g6",
            "Qg5", "Nc8", "hxg6", "hxg6", "Nh5", "Bc7", "Nf6+", "Kg7", "Qh4", "Bd8", "Ng5", "Bxf6", "exf6", "Kxf6",
            "Nh7+", "Kg7", "Nxf8", "Qe7", "Qh7+", "Kf6", "Qh8+", "Kg5", "g3", "Kg4", "Kg2", "Nd6", "f3+", "Kg5", "Qh4#"]

    game = ["e4", "c6", "Bc4", "d5", "exd5", "cxd5", "Bb5+", "Bd7", "Bxd7+", "Nxd7", "h3", "e5", "d3", "Ngf6", "Nf3",
            "Bc5", "O-O", "O-O", "Bg5", "h6", "Bxf6", "Qxf6", "Nc3", "d4", "Ne4", "Qb6", "Nxc5", "Qxc5", "c3", "dxc3",
            "bxc3", "Rac8", "d4", "Qxc3", "dxe5", "Nxe5", "Nxe5", "Qxe5", "Qd7", "Rc7", "Qa4", "b6", "Rfe1", "Qf6",
            "Rac1", "Rfc8", "Rxc7", "Rxc7", "Re8+", "Kh7", "Qe4+", "g6", "Qe3", "Qd6", "g3", "Rc1+", "Kg2", "Qd1",
            "Re7", "Qh1#"]

    game = ["e4", "Nc6", "Nf3", "d5", "exd5", "Qxd5", "Nc3", "Qh5", "d4", "Bg4", "Be2", "Nf6", "h3", "O-O-O", "O-O",
            "Bxh3", "gxh3", "Qxh3", "Ng5", "Qf5", "Bf3", "h6", "Nge4", "g5", "Nxf6", "Qxf6", "Bg2", "Nxd4", "Qg4+", "Nf5",
            "Be3", "a6", "Qf3", "e6", "Qxb7+", "Kd7", "Rad1+", "Ke8", "Qc6+", "Ke7", "Qxc7+", "Ke8", "Qc6+", "Ke7",
            "Bc5+", "Nd6", "Bxd6+", "Rxd6", "Qxd6+", "Ke8", "Qd7#"]

    game = ["e4", "e5", "Nf3", "Nf6", "Nc3", "Nc6", "g3", "Bc5", "d3", "d6", "Bg2", "a6", "h3", "Be6", "O-O",
            "Qd7", "Kh2", "O-O-O", "Na4", "Ba7", "Be3", "h6", "Bxa7", "Nxa7", "c4", "g5", "Ng1", "h5", "b4",
            "g4", "h4", "Rhg8", "Nc3", "Nh7", "a4", "f5", "exf5", "Bxf5", "b5", "axb5", "axb5", "b6", "Rxa7",
            "Kb8", "Qa4", "Qxb5", "Ra8#"]

    game = ["e4", "e6", "d4", "c5", "Nf3", "d6", "dxc5", "d5", "Bb5+", "Nc6", "exd5", "exd5", "O-O", "Bxc5", "Bg5", "Nf6",
            "Re1+", "Be6", "Nc3", "O-O", "Bxf6", "Qxf6", "Nxd5", "Bxd5", "Qxd5", "Bxf2+", "Kxf2", "Qxb2", "Bxc6", "bxc6",
            "Qxc6", "Rac8", "Qe4", "Rc2+", "Kg1", "Rg2+", "Kh1", "Rd8", "Qe8+", "Rxe8", "Rxe8#"]
            
    """

    game = ["e4", "c6", "Nf3", "d5", "exd5", "cxd5", "d4", "Nc6", "Bb5", "Nf6", "Nc3", "Bg4", "h3", "Bxf3", "Qxf3",
            "e6", "Bg5", "Be7", "O-O-O", "O-O", "h4", "a6", "Bxc6", "bxc6", "h5", "h6", "Bf4", "Bd6", "Qg3",
            "Bxf4", "Qxf4", "Qa5", "g4", "Rab8", "g5", "Ne4", "Nxe4", "dxe4", "gxh6", "f5", "hxg7", "Rf7", "h6",
            "Qxa2", "Rdg1", "Qxb2+", "Kd2", "Qb4+", "Ke2", "Qc4+", "Ke3", "Qc3+", "Ke2", "Qxc2+", "Qd2", "Qc4+", "Ke3", "Rb3+",
            "Kf4", "Rf3+", "Ke5", "Qd5#"]

    if COUNTER == move:
        return "z"

    COUNTER = COUNTER + 1

    print(game[move])
    return game[move]
