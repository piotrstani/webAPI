import api_github
import repo_visual


def main():
    repositories = api_github.get_github_repos(
        url=api_github.GITHUB_API_URL,
        headers=api_github.GITHUB_HEADERS,
        params=api_github.GITHUB_PARAMS
    )

    repo_links, stars, labels = (
        repo_visual.prepare_repos_stars_data(
            repositories
        )
    )

    fig = repo_visual.create_bar_chart(
        repo_links,
        stars,
        labels
    )

    repo_visual.save_chart(
        fig,
        "repo_visual.html"
    )


if __name__ == "__main__":
    main()