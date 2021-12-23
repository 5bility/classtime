// 2016152037 조현근 담당 영역입니다.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
	int i;
	char cmd[40];
	int arr[9];
	int cnt=7;
	int ret;

	for(i=0;i<9;i++)
		arr[i]=-1;

	for(i=1;i<9;i++)
		printf("%d   ",arr[i]);
	printf("\n\n");

	while(1)
	{
		for(i=1;i<=cnt+1;i++)
		{
			sprintf(cmd,"ping -c 1 10.0.42.%d | grep from",i);
			ret=system(cmd);
			if(WEXITSTATUS(ret)==0)   // ping-ack o
			{
				arr[i]=0;
			}
			else if(WEXITSTATUS(ret)==1)   // ping-ack x
			{
				arr[i]=1;
			}
		}
		
		for(i=1;i<=cnt+1;i++)
			printf("%d   ",arr[i]);

		for(i=1;i<=cnt+1;i++)
		{
			if(arr[i]==1)
			{
				if(i==2)
					system("docker start home");
				else if(i==3)
					system("docker start user");
				else if(i==4)
					system("docker start list");
				else if(i==5)
					system("docker start evaluation");
				else if(i==6)
					system("docker start community");
				else if(i==7)
					system("docker start grade");
				else if(i==8)
					system("docker start ct_mysql");
			}
		}
		printf("\n\n");
		sleep(1);
	}

	printf("\nfinish\n");

	return 0;

}
		
	
