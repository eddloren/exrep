    from google.cloud import gaming

    client = gaming.GameServerConfigsServiceClient()
    project_id = "your-project-id"

    # Location is hard coded as global, as game server configs can
    # only be created in global.
    request = gaming.ListGameServerConfigsRequest(
        parent=f"projects/{project_id}/locations/global"
    )
    page_result = client.list_game_server_configs(request=request)
    for game_server_config in page_result:
        print(game_server_config.name)  
