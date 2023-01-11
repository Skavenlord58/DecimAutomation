## DecimAutomation main functionality
# parsing the cronjob file

TARGETS = {
        "decimautomation" : "DecimAutomation#4633",
        "decimbot2": "DecimBOT 2.0#8467",
        "basedschizo" : "Based Schizo#7762"
    }

class Automaton:
    def __init__(self) -> None:
        pass

    def parse_cronjobs(self, path: str = "./cronjobs"):
        jobs: list = []
        with open(file=path, encoding="utf-8", mode="w") as file:
            for line in file.readlines():
                if line[0] == "#":
                    pass
                elif line[0] == "@":
                    jobs.append(line.split(" "))
        return jobs


    # working on jobs loop
    def precheck_jobs(self, jobs: list = None):
        for job in jobs:
            self.check_job_done(name=job[2], target=job[1], interval=job[0])
            if job[1] in TARGETS.keys:
                pass 
            pass

    # check if job was already done
    def check_job_done(self, name: str = None):
        with open():
            if name:
                pass

    # working on jobs loop
    def print_jobs(self, jobs: list = None):
        joblist = ""
        for job in jobs:
            joblist += f"Job {jobs.index(job)}: {job[0]} {job[1]} {job[2]}"
        return joblist

    # periodic job to check it's config
    def check_cronjobs(self):
        jobs: list = self.parse_cronjobs()
        return f"Job list parsed. Number of jobs: {len(jobs)}\nList of jobs:\n{self.print_jobs(jobs)}"

if __name__ == "__main__":
    pass