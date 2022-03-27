import imp
import json

from crosser import Crosser
from selector import Selector


class Configurer:
    @staticmethod
    def configure(file_name: str, population_size: int):
        with open(file_name, "r") as config_file:
            config = json.load(config_file)
            ## TODO: pasar todo a un archivo de configuración

            gen = 500
            if "gen" in config and int(config["gen"]) >= 500:
                gen = int(config["gen"])

            p = 0.01
            if "p" in config and 0 < config["p"] <= 1:
                p = config["p"]
            # a = 0.01
            # if "a" in config and 0 < config["a"] <= 1:
            #     a = config["a"]
            # tita = 0.01
            # if "o" in config and 0 < config["tita"] <= 1:
            #     tita = config["tita"]

            print("Selection: ", end="")
            selector = lambda population, size: Selector.direct_select(population, size)
            t0 = 80000
            tf = 60000
            k = 1
            u = 0.6
            trunc = 10
            if "selection" in config:
                if config["selection"] == "direct":
                    print("direct")
                    pass
                elif config["selection"] == "roulette":
                    print("roulette")
                    selector = lambda population, size: Selector.roulette_select(
                        population, size
                    )
                elif config["selection"] == "rank":
                    print("rank")
                    selector = lambda population, size: Selector.rank_select(
                        population, size
                    )
                elif config["selection"] == "tournament":
                    print("tournament", end=" ")
                    if "u" in config and 0.5 <= config["u"] <= 1:
                        u = config["u"]
                    print("[ u =", u, "]")
                    selector = lambda population, size: Selector.tournament_select(
                        population, size, u
                    )
                elif config["selection"] == "boltzman":
                    print("boltzman", end=" ")
                    if (
                        "k" in config
                        and 0 < k <= 1
                        and "t0" in config
                        and 0 < t0
                        and "tf" in config
                        and 0 < tf <= t0
                    ):
                        k = config["k"]
                        t0 = config["t0"]
                        tf = config["tf"]
                    print("[ k =", k, "| t0 =", t0, "| tf =", tf, "]")
                    selector = lambda population, size: Selector.boltzman_select(
                        population, size, gen, t0, tf, k
                    )
                elif config["selection"] == "truncate":
                    print("truncate", end=" ")
                    if "trunc" in config and 0 < trunc <= population_size:
                        trunc = config["trunc"]
                    print("[ truncate_k =", trunc, "]")
                    selector = lambda population, size: Selector.truncate_select(
                        population, size, trunc
                    )
                else:
                    raise "Invalid selection method"

            crosser = lambda first, second: Crosser.simple_cross(first, second)
            multiple_cross_n = 2
            if "cross" in config:
                print("Cross method: ", end="")
                if config["cross"] == "simple":
                    print("simple")
                    pass
                elif config["cross"] == "multiple":
                    print("multiple", end=" ")
                    if "multiple_cross_n" in config and config["multiple_cross_n"] > 1:
                        multiple_cross_n = config["multiple_cross_n"]
                    print("[ n =", multiple_cross_n, "]")
                    crosser = lambda first, second: Crosser.multiple_cross(
                        first, second, multiple_cross_n
                    )
                elif config["cross"] == "uniform":
                    print("uniform")
                    crosser = lambda first, second: Crosser.uniform_cross(first, second)
                else:
                    config_file.close()
                    raise "Invalid cross method"

        config_file.close()
        return {"gen": gen, "selector": selector, "crosser": crosser, "p": p}
