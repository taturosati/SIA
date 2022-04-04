import json

from crosser import Crosser
from selector import Selector


class Configurer:
    @staticmethod
    def configure(file_name: str, genome_size: int):
        with open(file_name, "r") as config_file:
            config = json.load(config_file)

            population_size = 500
            if "p_size" in config and int(config["p_size"]) >= 10:
                population_size = int(config["p_size"])
            print("Population size:", population_size)

            gen = 500
            if "gen" in config and int(config["gen"]) >= 500:
                gen = int(config["gen"])
            print("Min gen simulation:", gen)

            p = 0.01
            if "p" in config and 0 < config["p"] <= 1:
                p = config["p"]
            print("Mutation probability P:", p)

            print("Selection method: ", end="")
            selector = lambda population, size: Selector.direct_select(population, size)
            t0 = 10000
            tf = 8000
            k = 10
            u = 0.6
            trunc = 10
            if "selection" in config:
                title = config["selection"]
                if config["selection"] == "direct":
                    print("direct")
                    pass
                elif config["selection"] == "roulette":
                    print("roulette")
                    selector = lambda population, size: Selector.roulette_select(population, size)
                elif config["selection"] == "rank":
                    print("rank")
                    selector = lambda population, size: Selector.rank_select(population, size)
                elif config["selection"] == "tournament":
                    print("tournament", end=" ")
                    if "u" in config and 0.5 <= config["u"] <= 1:
                        u = config["u"]
                    
                    title += " - u = " + str(u)
                    print("[ u =", u, "]")
                    selector = lambda population, size: Selector.tournament_select(population, size, u)
                elif config["selection"] == "boltzmann":
                    print("boltzmann", end=" ")
                    if ("k" in config and "t0" in config
                            and 0 < t0 and "tf" in config and 0 < tf <= t0):
                        k = config["k"]
                        t0 = config["t0"]
                        tf = config["tf"]
                    
                    title += " - k = " + str(k) + " - t0 = " + str(t0) + " - tf = " + str(tf)
                    print("[ k =", k, "| t0 =", t0, "| tf =", tf, "]")
                    selector = lambda population, size: Selector.boltzmann_select(population, size, gen,
                                                                                  t0, tf, k)
                elif config["selection"] == "truncate":
                    print("truncate", end=" ")
                    if "trunc" in config and 0 < trunc <= genome_size:
                        trunc = config["trunc"]
                    
                    title += " trunc = " + str(trunc)
                    print("[ truncate_k =", trunc, "]")
                    selector = lambda population, size: Selector.truncate_select(population, size, trunc)
                else:
                    raise "Invalid selection method"

            crosser = lambda first, second: Crosser.simple_cross(first, second, genome_size)
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
                    crosser = lambda first, second: Crosser.multiple_cross(first, second,
                                                                           multiple_cross_n, genome_size)
                elif config["cross"] == "uniform":
                    print("uniform")
                    crosser = lambda first, second: Crosser.uniform_cross(first, second, genome_size)
                else:
                    config_file.close()
                    raise "Invalid cross method"

        config_file.close()
        return {"p_size": population_size, "gen": gen, "selector": selector, "crosser": crosser, "p": p, "title": title}
