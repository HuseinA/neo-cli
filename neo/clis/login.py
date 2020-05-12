from neo.clis.base import Base
from neo.libs import login as login_lib
from neo.libs import utils
from tabulate import tabulate


class Login(Base):
    """
    Usage:
        login
        login -D | --describe
        login [-u USERNAME] [-r REGION]


    Options:
    -h --help                                       Print usage
    -D --describe                                   Set your desired domain URL
    -r REGION --region=REGION                       Pick your region, to get list of region use neo --region      
    -u USERNAME --username=USERNAME                 Set your desired username
    """

    def execute(self):
        if self.args["--describe"]:
            envs = login_lib.get_env_values()
            try:
                env_data = [
                    [
                        envs["username"],
                        envs["auth_url"],
                        envs["project_id"],
                        envs["user_domain_name"],
                    ]
                ]
            except:
                exit()

            if len(env_data) == 0:
                utils.log_err("No Data...")
                print(self.__doc__)
                exit()

            print(
                tabulate(
                    env_data,
                    headers=["Username", "Auth URL", "Project ID", "Domain Name"],
                    tablefmt="grid",
                )
            )
            exit()

        if not self.args["--region"] and not self.args["--username"]:
            login_lib.do_login2()
        else:
            login_lib.do_login2(
                username=self.args["--username"], region=self.args["--region"]
            )


"""         if self.args["--domain"] and self.args["--keystone-url"]:
            try:
                username = self.args["--username"]
                auth_url = self.args["--keystone-url"]
                user_domain_name = self.args["--domain"]
                login_lib.do_login(
                    auth_url=auth_url,
                    user_domain_name=user_domain_name,
                    username=username,
                )
            except Exception as e:
                utils.log_err(e) """
