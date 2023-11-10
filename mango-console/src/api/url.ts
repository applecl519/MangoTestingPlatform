import { baseURL } from './axios.config'

export const baseAddress = baseURL

// 项目原始接口
export const updateUserInfo = '/updateUser'
export const deleteUserById = '/deleteUserById'
export const addDepartment = '/addDepartment'
export const getParentMenuList = '/getParentMenuList'
export const getCardList = '/getCardList'
export const getCommentList = '/getCommentList'
export const addUserInfo = '/addUser'

// 修改原始接口后的
export const login = '/login'
export const getMenuListByRoleId = '/menu/'
export const getAllMenuByRoleId = '/role'
export const getMenuList = '/menu_1'
export const test = '/testconfig/test'
// -
export const getDepartmentList = '/user/project'
export const getRoleList = '/user/role'
export const getAllRole = '/user/role/all'

export const getUserList = '/user/user'
export const getUserQuery = '/user/user/query'
export const getAllItems = '/user/project/all'
export const getNickname = '/user/get/nickname/'
export const getProjectModuleGetAll = '/user/project/module/get/all'

// -
export const ApiCase = '/api/case'
export const ApiCaseGroup = '/api/case/group'
export const ApiPublic = '/api/public'
export const GetHeader = '/api/public/header'
export const ApiRelyOn = '/api/relyon'
export const ApiPublicEnd = '/api/public/end'
export const ApiPublicPublic = '/api/public/public'
export const ApiRun = '/api/run'
export const ApiCaseSynchronous = '/api/case/synchronous'

// -
export const uiPage = '/ui/page'
export const uiPageQuery = '/ui/page/query'
export const uiPageNameAll = '/ui/page/name/all'
export const uiPageNameProject = '/ui/page/name/project'
export const uiUiElement = '/ui/element'
export const uiUiElementName = '/ui/element/name'
export const getUiElementExp = '/ui/element/exp'
export const uiSteps = '/ui/steps'
export const uiStepsQuery = '/ui/steps/query'
export const uiStepsPutType = '/ui/steps/put/type'
export const uiStepsPageStepsName = '/ui/steps/get/page/steps/name'
export const uiCase = '/ui/case'
export const uiCaseQuery = '/ui/case/query_by'
export const uiCaseRun = '/ui/case/run'

export const uiCaseStepsDetailed = '/ui/case/steps/detailed'
export const uiCaseStepsRefreshCacheData = '/ui/case/steps/refresh/cache/data'
export const uiPageStepsDetailed = '/ui/page/steps/detailed'
export const uiPageStepsDetailedAss = '/ui/page/steps/detailed/ass'
export const uiPageStepsDetailedOpe = '/ui/page/steps/detailed/ope'
export const uiPageAssMethod = '/ui/page/ass/method'
export const UiStepsRun = '/ui/steps/run'
export const uiRunCaseBatch = 'ui/case/batch/run'
export const uiConfig = '/ui/config'
export const uiConfigGetBrowserType = '/ui/config/get/browser/type'
export const uiConfigGetDriveType = '/ui/config/get/drive/type'
export const uiConfigPutState = '/ui/config/put/state'
export const uiConfigNewBrowserObj = '/ui/config/new/browser/obj'
export const getCaseNaneList = '/ui/get/case/name/list'
export const uiPublic = '/ui/public'
export const uiPublicQuery = '/ui/public/query'
export const uiPublicPutState = '/ui/public/put/state'
export const uiCaseResultSuiteGetCase = '/ui/case/result/suite/get/case'
export const uiEleResultEle = '/ui/ele/result/ele'

// -
export const getProjectConfig = '/system/test/object'
export const getTestObjQuery = '/system/test/object/query'
export const getEnvironmentEnum = '/system/get/environment/enum'
export const getTestObjName = '/system/get/test/obj/name'
export const getAutoTestName = '/system/get/aut1o/te1st/name'
export const getPlatformEnum = '/system/get/platform/enum'
export const getNoticeConfig = '/system/notice'
export const getNoticeConfigQuery = '/system/notice/query'
export const getNoticeType = '/system/notice/type'
export const getNoticePutState = '/system/notice/put/state'
export const getDatabase = '/system/database'
export const getDatabaseQuery = '/system/database/query'
export const getDatabasePutState = '/system/database/put/state'
export const getRandomList = 'system/variable/random/list'
export const getRandomData = 'system/variable/value'
export const getTimeList = 'system/time'
export const getTimeQuery = 'system/time/query'
export const triggerTiming = 'system/trigger/timing'
export const getScheduledTasks = 'system/scheduled/tasks'
export const getScheduledTasksQuery = 'system/scheduled/tasks/query'
export const getScheduledTasksPutState = 'system/scheduled/put/state'
export const getTasksRunCase = 'system/tasks/run/case'
export const getTasksTypeCaseName = 'system/tasks/type/case/name'
export const SocketUserList = 'system/socket/user/list'
export const SocketAllUserSum = 'system/socket/all/user/sum'
export const getTimingList = 'system/get/timing/list'
export const getNoticeTest = 'system/notice/test'
export const sendCommonParameters = 'system/send/common/parameters'
export const testSuiteReport = 'system/test/suite/report'
export const testSuiteAllReportSum = 'system/test/suite/all/report/sum'
export const testSuiteAllCaseSum = 'system/test/suite/all/case/sum'
export const getCacheKeyValue = 'system/get/cache/key/value'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $urlPath: Record<string, string>
  }
}
